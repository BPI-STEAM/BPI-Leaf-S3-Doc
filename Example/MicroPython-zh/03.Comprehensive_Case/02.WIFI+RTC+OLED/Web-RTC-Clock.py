from machine import I2C,Pin,RTC
from ssd1306 import SSD1306_I2C
from neopixel import NeoPixel
import time,network
import urequests

SSID = "wifi-ssid"
PASSWORD = "wifi-password"
Url = "http://worldtimeapi.org/api/timezone/Asia/Hong_Kong"
week_list=["Mon.","Tue.","Wed.","Thu.","Fri.","Sat.","Sun."]

rtc = RTC()
print(rtc.datetime())

sda_pin=Pin(15,Pin.PULL_UP)
scl_pin=Pin(16,Pin.PULL_UP)

i2c = I2C(1,sda=sda_pin, scl=scl_pin, freq=800_000)
print(i2c.scan())
oled = SSD1306_I2C(128, 64, i2c, addr=0x3c)
    
def display():
    datetime=rtc.datetime()
    oled.fill(0)
    oled.text("{0}/{1:0>2d}/{2:0>2d}<{3}>".format(datetime[0],datetime[1],datetime[2],week_list[datetime[3]]), 0,  0)
    oled.text("{0:0>2d}:{1:0>2d}:{2:0>2d}".format(datetime[4],datetime[5],datetime[6]), 32,  8)
    oled.show()

def ConnectNet():
    pin_48 = Pin(48, Pin.OUT)#Use GPIO48 as the signal line of WS2812
    np = NeoPixel(pin_48, 1,bpp=3, timing=1)
    np[0] = (25,0,0)
    np.write()
    try:
        wifi = network.WLAN(network.STA_IF)#Create a network interface
        wifi.active(True)#activate interface
        print(wifi.scan())#Output scanned SSID
        if not wifi.isconnected():
            wifi.connect(SSID,PASSWORD)#Connect to the specified SSID
            print('start to connect wifi')
            oled.text("WiFi connect", 0,  0)
            oled.show()
            for i in range(30):
                print('try to connect wifi in {}s'.format(i))
                oled.text(".", 12*8+i*4,  0)
                oled.show()
                time.sleep(1)
                if wifi.isconnected():
                    oled.fill(0)
                    break
        if wifi.isconnected():
            np[0] = (0,25,0)
            np.write()
            print('WiFi connection OK!')
            print('Network Config=',wifi.ifconfig())#Get and print the  IP address, subnet mask, gateway and DNS server.
            oled.text("WiFi connect!IP:", 0,  0)
            oled.text("{}".format(wifi.ifconfig()[0]), 0,  8)
            oled.show()
            time.sleep_ms(1500)
            np[0] = (0,0,0)
            np.write()
        else:
            print('WiFi connection Error')
    except Exception as e: print(e)

def net_rtc():
    requests = urequests.get(Url)#Open the URL to get information through the urequests module
    print(requests.text)#Output all acquired information in text form
    parsed = requests.json()#Convert to json format for separating out the information
    datetime_str = str(parsed["datetime"])#Extract datetime information and save to variable as string format
    year = int(datetime_str[0:4])#String slices and save to their corresponding variables
    month = int(datetime_str[5:7])
    day = int(datetime_str[8:10])
    #weekday=str(parsed["day_of_week"])
    hour = int(datetime_str[11:13])
    minute = int(datetime_str[14:16])
    second = int(datetime_str[17:19])
    subsecond = int(round(int(datetime_str[20:26]) / 10000))

    rtc.datetime((year, month, day, 0, hour, minute, second, subsecond))#Update internal RTC
    print(rtc.datetime())
    print("RTC updated\n")

ConnectNet()
net_rtc()
while True:
    display()
    time.sleep_ms(100)