from machine import Pin, PWM
import time

PWM_LED = PWM(Pin(13))#从GPIO13引脚中创建PWM对象
PWM_LED.freq(1000)#设置频率
PWM_LED.duty(0)#设置占空比，0≤duty≤1023，10bit精度

while True:
    for i in range(0,1024,1):
       PWM_LED.duty(i)
       time.sleep_ms(2)
    for i in range(1022,0,-1):
       PWM_LED.duty(i)
       time.sleep_ms(1)
    #修改sleep_ms参数可改变LED“呼吸”频率