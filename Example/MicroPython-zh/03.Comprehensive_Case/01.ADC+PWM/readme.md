# 使用ADC测量电位器，用以调整电机转速

## 外部硬件需求

* 电位器 x 1
* TB6612FNG电机驱动模块 x 1
* 5v直流电机 x 1
* 一些连接线材

## 连接方法

|Potentiometer|BPI-Leaf-S3|
|---|---|
|GND|GND|
|VCC|3V3|
|S|14|

|TB6612FNG|BPI-Leaf-S3|
|---|---|
|PWMA|11|
|AIN2|13|
|AIN1|12|
|STBY|10|
|VM|5V|
|VCC|3.3V|
|GND|GND|

|TB6612FNG|Motor|
|---|---|
|AO1|Motor N pole|
|AO2|Motor S pole|

## 运行效果

开发板将间隔100ms在REPL输出ADC读取到的电压值，单位为mv，以及对应控制的PWM占空比。

用手调整电位器，改变其输出电压，电压越大，开发板输出的PWM占空比越高，电机转速越快。