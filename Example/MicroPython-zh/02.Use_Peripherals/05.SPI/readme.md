# SPI MAX7219 8X8LED点阵显示

## 外部硬件需求

一个MAX7219 8X8LED点阵模块。

![](https://i.imgur.com/H12i0OH.jpg)

## 连接方法

MAX7219的VCC接Leaf-S3的3V3，GND接GND，DIN接GPIO10，CS接GPIO11，CLK接GPIO12。

可以自行选择任意的没有被其他功能占用的GPIO作为SPI接口。

## 运行效果

在运行 `05.SPI.py` 前确保 `max7219.py` 文件已上传至开发板，此文件为MAX7219的驱动模块。

LED点阵将以0.5秒的时间间隔循环显示大写英文字母 A 至 Z 。