# UART 串口数据读写

## 外部硬件需求

USB转UART模块（CH340，CP2102等）。

## 软件需求

一个串口调试软件以及USB转UART模块所需驱动。

## 连接方法

将BPI-Leaf-S3开发板通过USB连接电脑，USB转UART模块的RX接GPIO17（BPI-Leaf-S3的TX），TX接GPIO18（BPI-Leaf-S3的RX），GND接GND（共地），USB转UART模块的USB接口连接电脑，可以是连接BPI-Leaf-S3的同一台电脑，也可以是不同的两台电脑。

## 运行效果

在BPI-Leaf-S3所在电脑的MicroPython REPL中将间隔一秒输出一次从USB转UART模块中接收到的字符数据。

而在USB转UART模块所在的电脑的串口调试软件窗口中则可以看到，每间隔一秒输出一行由BPI-Leaf-S3发送的字符 `Hello World!` 。