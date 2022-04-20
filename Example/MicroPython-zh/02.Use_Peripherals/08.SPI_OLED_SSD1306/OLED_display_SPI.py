from machine import SPI,Pin
from ssd1306 import SSD1306_SPI

D0_sck=Pin(9)
D1_mosi=Pin(10)
RES=Pin(11)
DC=Pin(12)
CS=Pin(13)

spi =  SPI(2,baudrate=20000000,sck=D0_sck,mosi=D1_mosi,miso=None)
oled = SSD1306_SPI(128, 64, spi, dc=DC,res=RES, cs=CS)

def display():
    #framebuf库只支持编码为32~126的ASCII打印字符
    oled.text(" !\"#$%&'()*+,-./", 0,  0)
    oled.text("0123456789:;<=>?", 0,  8)
    oled.text("@ABCDEFGHIJKLMNO", 0, 16)
    oled.text("PQRSTUVWXYZ[\]^_", 0,  24)
    oled.text("`abcdefghijklmno",0, 32)
    oled.text("pqrstuvwxyz{|}~",0, 40)
    oled.show()

def testAscii():
    # chr()返回值是当前整数对应的 ASCII 字符
    Ascii = ''
    for i in range(32,127):
        Ascii = Ascii + chr(i)
    for i in range(128,256):
        Ascii = Ascii + chr(i)
    return Ascii

def display_Ascii():
    #framebuf库只支持编码为32~126的ASCII打印字符
    oled.text(testAscii()[0:16], 0,  0)
    oled.text(testAscii()[16:32],0,  8)
    oled.text(testAscii()[32:48],0, 16)
    oled.text(testAscii()[48:64],0, 24)
    oled.text(testAscii()[64:80],0, 32)
    oled.text(testAscii()[80:95],0, 40)
    oled.show()

if __name__=="__main__":
    display()
    #display_Ascii()