from machine import Pin,time_pulse_us
import time
trig = Pin(1,Pin.OUT,pull=None)
echo = Pin(2,Pin.IN,pull=Pin.PULL_DOWN)
while True:
    trig.value(0)
    time.sleep_us(5)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    echo_pulse_time = time_pulse_us(echo,1,80_000)
    print("echo_pulse_time=%sus" % (echo_pulse_time))
    distance = echo_pulse_time / 1_000_000 *34_000 / 2
    print("distance=%scm" % (distance))
    time.sleep_ms(100)