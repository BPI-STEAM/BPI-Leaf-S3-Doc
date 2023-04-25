from machine import UART
import time

uart1 = UART(1, tx=17, rx=18)
# Select the UART interface and specify the pins used by TX and RX

uart1.init(115200, bits=8, parity=None, stop=1)
# Initialization, set the baud rate, set the number of characters, set the parity, set the stop bit


def test():
    for i in range(50):
        uart1.write('Hello World!')  # write data
        time.sleep(0.5)
        print(uart1.read())  # read data
        time.sleep(0.5)


test()
