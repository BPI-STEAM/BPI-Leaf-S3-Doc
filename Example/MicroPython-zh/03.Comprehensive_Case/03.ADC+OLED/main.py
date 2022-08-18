from machine import Pin,ADC,I2C
from ssd1306 import SSD1306_I2C
import time

adc1 = ADC(Pin(1),atten=ADC.ATTN_11DB)

sda_pin=Pin(15,Pin.PULL_UP)
scl_pin=Pin(16,Pin.PULL_UP)

i2c = I2C(1,sda=sda_pin, scl=scl_pin, freq=800_000)
print(i2c.scan())
oled = SSD1306_I2C(128, 64, i2c, addr=0x3c)

#Init, white background
oled.fill(1)
oled.rect(0,32,128,10,0)

while True:
    #Read ADC
    adc1_read = adc1.read() # 12bit
    adc1_read_mv = adc1.read_uv()//1000
    adc1_read_u16 = adc1.read_u16() # 16bit
    
    #Set progress bar
    bar_width = round (adc1_read / 4095 * 128)
    oled.fill_rect(bar_width,33,128-bar_width,8,0)
    oled.fill_rect(0,33,bar_width,8,1)
    
    #Set ADC text, centered
    text_adc1 = str(adc1_read_mv) + " mV"
    start_x_text_adc1 = 64 - len(text_adc1)*4
    oled.fill_rect(36,24,56,8,1)
    oled.text(text_adc1,start_x_text_adc1,24,0)
    
    #Show
    oled.show()
    
    print(adc1_read,adc1_read_u16,adc1_read_mv,"mv",bar_width,"width")
    time.sleep(0.05)