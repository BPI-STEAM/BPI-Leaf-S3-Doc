from machine import Pin,ADC,PWM
import time

adc14 = ADC(Pin(14),atten=ADC.ATTN_11DB)

PWM_A = PWM(Pin(11)) #Set PWM output pin
PWM_A.freq(20000) #Set PWM frequency
PWM_A.duty(0) #Set PWM duty cycle
AIN1 = Pin(12,Pin.OUT)
AIN2 = Pin(13,Pin.OUT)
STBY = Pin(10,Pin.OUT)
AIN1.on() #MOTOR forward
AIN2.off()
STBY.on() #When STBY pin is at high level, TB6612FNG starts.

while True:
    read_mv=adc14.read_uv()//1000
    if read_mv <= 3000:
        duty_set = int(1023/3000 * read_mv)
    else:
        duty_set = 1023
    PWM_A.duty(duty_set)
    Duty_cycle = int(duty_set/1023*100)
    print("ADC_read={0}mv,Duty_cycle={1}%".format(read_mv,Duty_cycle))
    time.sleep_ms(100)
