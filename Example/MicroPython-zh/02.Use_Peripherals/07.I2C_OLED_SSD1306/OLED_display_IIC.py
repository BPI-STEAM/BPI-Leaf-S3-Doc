from machine import I2C, Pin
from ssd1306 import SSD1306_I2C

sda_pin = Pin(15, Pin.PULL_UP)
scl_pin = Pin(16, Pin.PULL_UP)

i2c = I2C(1, sda=sda_pin, scl=scl_pin, freq=800_000)
print(i2c.scan())
oled = SSD1306_I2C(128, 64, i2c, addr=0x3c)


def display():
    # The framebuf library only supports ASCII printing characters encoded as 32~126
    oled.text(" !\"#$%&'()*+,-./", 0,  0)
    oled.text("0123456789:;<=>?", 0,  8)
    oled.text("@ABCDEFGHIJKLMNO", 0, 16)
    oled.text("PQRSTUVWXYZ[\]^_", 0,  24)
    oled.text("`abcdefghijklmno", 0, 32)
    oled.text("pqrstuvwxyz{|}~", 0, 40)
    oled.show()


def testAscii():
    # The return value of chr() is the ASCII character corresponding to the current integer
    Ascii = ''
    for i in range(32, 127):
        Ascii = Ascii + chr(i)
    for i in range(128, 256):
        Ascii = Ascii + chr(i)
    return Ascii


def display_Ascii():
    # The framebuf library only supports ASCII printing characters encoded as 32~126
    oled.text(testAscii()[0:16], 0,  0)
    oled.text(testAscii()[16:32], 0,  8)
    oled.text(testAscii()[32:48], 0, 16)
    oled.text(testAscii()[48:64], 0, 24)
    oled.text(testAscii()[64:80], 0, 32)
    oled.text(testAscii()[80:95], 0, 40)
    oled.show()


if __name__ == "__main__":
    display()
    # print(testAscii())
    # display_Ascii()

# ASCII printing characters (character encoding: 32-127)
# 32~126 (95 in total) are characters: 32 is a space, among which 48~57 are ten Arabic numerals from 0 to 9,
# 65～90 are 26 uppercase English letters,
# 97~122 are 26 lowercase English letters,
# The rest are some punctuation marks, operation symbols, etc.
# The 127th character represents the delete command on the keyboard.
# ASCII extension code (character encoding: 128-255)
# The last 128 are called extended ASCII codes.
# Many x86-based systems support the use of extended (or "high") ASCII.
# The extended ASCII code allows the 8th bit of each character 
# to be used to determine additional 128 special symbol characters, foreign language letters and graphic symbols.
