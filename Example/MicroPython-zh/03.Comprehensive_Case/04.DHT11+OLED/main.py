from machine import Pin,I2C
from ssd1306 import SSD1306_I2C
import time
import dht

dht11 = dht.DHT11(Pin(1))

sda_pin=Pin(15,Pin.PULL_UP)
scl_pin=Pin(16,Pin.PULL_UP)

i2c = I2C(1,sda=sda_pin, scl=scl_pin, freq=800_000)
print(i2c.scan())
oled = SSD1306_I2C(128, 64, i2c, addr=0x3c)

#Init, white background
oled.fill(1)
oled.rect(0,22,128,10,0)
oled.rect(0,53,128,10,0)

while True:
    #Read DHT11
    dht11.measure() # Measure and read data once.
    temperature = dht11.temperature() # -20℃ ~ 60℃
    humidity = dht11.humidity() # 5%RH ~ 95%RH
    
    #Set temperature text, centered
    text_1 = str(temperature) + " C"
    start_x_1 = 64 - len(text_1)*4
    oled.fill_rect(0,14,128,8,1)
    oled.text(text_1,start_x_1,14,0)
    
    #Set temperature bar
    bar_1 = round ((temperature+20)/80 * 128)
    oled.fill_rect(bar_1,23,128-bar_1,8,0)
    oled.fill_rect(0,23,bar_1,8,1)
    
    #Set humidity text, centered
    text_2 = str(humidity) + " %RH"
    start_x_2 = 64 - len(text_2)*4
    oled.fill_rect(0,45,128,8,1)
    oled.text(text_2,start_x_2,45,0)
    
    #Set humidity bar
    humidity_bar = round (humidity/100 * 128)
    oled.fill_rect(humidity_bar,54,128-humidity_bar,8,0)
    oled.fill_rect(0,54,humidity_bar,8,1)
    
    #Show
    oled.show()
    
    print("Temperature={0}℃,Humidity={1}%RH".format(temperature,humidity))
    time.sleep(2.5)