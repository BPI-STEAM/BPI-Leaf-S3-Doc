from machine import I2C,Pin

sda_pin=Pin(15,Pin.PULL_UP)
scl_pin=Pin(16,Pin.PULL_UP)

i2c = I2C(1,sda=sda_pin, scl=scl_pin, freq=400_000)
i2c_list=i2c.scan()
i2c_total=len(i2c_list)
print("Total num:",i2c_total)
j=0
for i in i2c_list:
    j=j+1
    print("NO.{0},address:{1}".format(j,hex(i)))