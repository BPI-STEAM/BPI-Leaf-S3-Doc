from machine import I2C,Pin
from ssd1306 import SSD1306_I2C

sda_pin=Pin(15,Pin.PULL_UP)
scl_pin=Pin(16,Pin.PULL_UP)

i2c = I2C(1,sda=sda_pin, scl=scl_pin, freq=800_000)
print(i2c.scan())
oled = SSD1306_I2C(128, 64, i2c, addr=0x3c)
    
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
    #print(testAscii())
    #display_Ascii()
    
#ASCII 打印字符 (字符编码: 32-127)
#32～126(共95个)是字符：32是空格，其中48～57为0到9十个阿拉伯数字，
#65～90为26个大写英文字母，
#97～122号为26个小写英文字母，
#其余为一些标点符号、运算符号等。
#第127个字符表示的是键盘上的删除命令。
#ASCII扩展码 (字符编码: 128-255)
#后128个称为扩展ASCII码。
#许多基于x86的系统都支持使用扩展（或“高”）ASCII。
#扩展ASCII码允许将每个字符的第8 位用于确定附加的128 个特殊符号字符、外来语字母和图形符号。
        
