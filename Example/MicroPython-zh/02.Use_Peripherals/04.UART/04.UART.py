from machine import UART
import time

uart1 = UART(1, tx=17, rx=18)
#选择UART接口，指定TX与RX使用的引脚

uart1.init(115200, bits=8, parity=None, stop=1)
#初始化，设置波特率，设置字符位数，设置奇偶校验，设置停止位

def test():
    for i in range(50):
        uart1.write('Hello World!')#写数据
        time.sleep(0.5)
        print(uart1.read())#读数据
        time.sleep(0.5)

test()