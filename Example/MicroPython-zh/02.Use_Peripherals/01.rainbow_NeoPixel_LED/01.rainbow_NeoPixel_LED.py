from machine import Pin
from neopixel import NeoPixel
import time

def rainbow(num=1,level=25,delay=100):
    #num:设置循环彩灯的数量
    #level:设置亮度等级，范围 0~255
    #delay:设置每次变化时间间隔，单位ms
    def write_all(num,delay,red,green,blue):
        for j in range (num):
            np[j] = (red,green,blue)
        np.write()
        time.sleep_ms(delay)
    
    red,green,blue = level,0,0
    
    rainbow_step_list2 = [(0,1,0),(-1,0,0),(0,0,1),(0,-1,0),(1,0,0),(0,0,-1)]
    
    for step in rainbow_step_list2:
        for i in range (level):
            red+=step[0]
            green+=step[1]
            blue+=step[2]
            write_all(num,delay,red,green,blue)
            #print(red,green,blue)

pin_48 = Pin(48, Pin.OUT)#将GPIO48作为WS2812的信号传输线
np = NeoPixel(pin_48, 1,bpp=3, timing=1)
# 在GPIO48上创建一个NeoPixel对象，设置数量1，bpp=3为RGB模式，4为RGBW模式，timing=1为800kHz，0为400kHz

while True:
    #彩虹灯循环
    rainbow(num=1,level=25,delay=10)
    #print("RAM used = {RAM_used}KB".format(RAM_used = gc.mem_alloc()/1024))
    #gc.collect()
