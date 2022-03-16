from machine import Pin
from neopixel import NeoPixel
import time 
pin_48 = Pin(48) #BPI-Leaf-S3 板载的一颗 NeoPixel LED 在 GPIO48 上
np = NeoPixel(pin_48, 1,bpp=3, timing=1)# 初始化NeoPixel
while True:
    np[0] = (25,25,25) #三色相同即亮白光
    np.write() #输出显示
    time.sleep_ms(250) #间隔250ms
    np[0] = (0,0,0) #灭灯
    np.write()
    time.sleep_ms(250)