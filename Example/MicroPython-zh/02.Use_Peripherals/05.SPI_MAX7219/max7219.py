from machine import Pin
from micropython import const
import framebuf
"""
Driver for MAX7219 8x8 LED matrices
Inheritance for FrameBuffer:
self.fill  # (col)
self.pixel # (x, y[, c])
self.hline  # (x, y, w, col)
self.vline  # (x, y, h, col)
self.line  # (x1, y1, x2, y2, col)
self.rect  # (x, y, w, h, col)
self.fill_rect  # (x, y, w, h, col)
self.text  # (string, x, y, col=1)
self.scroll  # (dx, dy)
self.blit  # (fbuf, x, y[, key])

Example for ESP8266 with 2x4 matrices (one on top, one on bottom),
so we have a 32x16 display area:
>>> from machine import Pin, SPI
>>> from max7219 import Max7219
>>> spi = SPI(1, baudrate=10000000)
>>> screen = Max7219(32, 16, spi, Pin(15))
>>> screen.rect(0, 0, 32, 16, 1)  # Draws a frame
>>> screen.text('Hi!', 4, 4, 1)
>>> screen.show()
On some matrices, the display is inverted (rotated 180°), in this case
 you can use `rotate_180=True` in the class constructor.

"""
    
_DIGIT_0 = const(0x1)

_DECODE_MODE = const(0x9)
_NO_DECODE = const(0x0)

_INTENSITY = const(0xA)
_INTENSITY_MIN = const(0x0)

_SCAN_LIMIT = const(0xB)
_DISPLAY_ALL_DIGITS = const(0x7)

_SHUTDOWN = const(0xC)
_SHUTDOWN_MODE = const(0x0)
_NORMAL_OPERATION = const(0x1)

_DISPLAY_TEST = const(0xF)
_DISPLAY_TEST_NORMAL_OPERATION = const(0x0)

_MATRIX_SIZE = const(8)


class Max7219(framebuf.FrameBuffer):

    def __init__(self, width, height, spi, cs, rotate_180=False):
        # Pins setup
        self.spi = spi
        self.cs = cs
        self.cs.init(Pin.OUT, True)

        # Dimensions
        self.width = width
        self.height = height
        # Guess matrices disposition
        self.cols = width // _MATRIX_SIZE
        self.rows = height // _MATRIX_SIZE
        self.nb_matrices = self.cols * self.rows
        self.rotate_180 = rotate_180

        # 1 bit per pixel (on / off) -> 8 bytes per matrix
        self.buffer = bytearray(width * height // 8)
        format = framebuf.MONO_HLSB if not self.rotate_180 else framebuf.MONO_HMSB
        super().__init__(self.buffer, width, height, format)

        # Init display
        self.init_display()

    def _write_command(self, command, data):
        """Write command on SPI"""
        cmd = bytearray([command, data])
        self.cs(0)
        for matrix in range(self.nb_matrices):
            self.spi.write(cmd)
        self.cs(1)

    def init_display(self):
        """Init hardware"""
        for command, data in (
            (_SHUTDOWN, _SHUTDOWN_MODE),  # Prevent flash during init
            (_DECODE_MODE, _NO_DECODE),
            (_DISPLAY_TEST, _DISPLAY_TEST_NORMAL_OPERATION),
            (_INTENSITY, _INTENSITY_MIN),
            (_SCAN_LIMIT, _DISPLAY_ALL_DIGITS),
            (_SHUTDOWN, _NORMAL_OPERATION),  # Let's go
        ):
            self._write_command(command, data)

        self.fill(0)
        self.show()

    def brightness(self, value):
        """Set display brightness (0 to 15)"""
        if not 0 <= value < 16:
            raise ValueError("Brightness must be between 0 and 15")
        self._write_command(_INTENSITY, value)

    def show(self):
        """Update display"""
        # Write line per line on the matrices
        for line in range(8):
            self.cs(0)

            for matrix in range(self.nb_matrices):
                # Guess where the matrix is placed
                row, col = divmod(matrix, self.cols)
                # Compute where the data starts
                if not self.rotate_180:
                    offset = row * 8 * self.cols
                    index = col + line * self.cols + offset
                else:
                    offset = 8 * self.cols - row * (8 - line) * self.cols
                    index = (7 - line) * self.cols + col - offset

                self.spi.write(bytearray([_DIGIT_0 + line, self.buffer[index]]))

            self.cs(1)