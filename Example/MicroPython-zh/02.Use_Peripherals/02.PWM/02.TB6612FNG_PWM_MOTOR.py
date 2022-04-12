from machine import Pin,PWM
import time

PWM_A = PWM(Pin(11)) #Set PWM output pin
PWM_A.freq(20000) #Set PWM frequency
PWM_A.duty(0) #Set PWM duty cycle
AIN1 = Pin(12,Pin.OUT)
AIN2 = Pin(13,Pin.OUT)
STBY = Pin(10,Pin.OUT)
STBY.on() #When STBY pin is at high level, TB6612FNG starts.

def MOTOR_Forward():
    AIN1.on()
    AIN2.off()
def MOTOR_Reverse():
    AIN1.off()
    AIN2.on()

while True:
    MOTOR_Forward()
    #for cycle is used to control the PWM duty cycle change.
    #The PWM duty cycle control precision is 10bit, ie 0~1023.
    #Some motors require a certain PWM duty cycle to start.
    for i in range(350,1024,1):
       PWM_A.duty(i)
       time.sleep_ms(10)
    for i in range(1022,0,-1):
       PWM_A.duty(i)
       time.sleep_ms(5)
    
    MOTOR_Reverse()
    for i in range(350,1024,1):
       PWM_A.duty(i)
       time.sleep_ms(10)
    for i in range(1022,0,-1):
       PWM_A.duty(i)
       time.sleep_ms(5)
