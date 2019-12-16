#!/usr/bin/env python
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import time

LED="P9_14"
button1="P9_23"
button2="P9_27"
#Setup buttons
GPIO.setup(button1, GPIO.IN)
GPIO.setup(button2, GPIO.IN)
#start PWM
PWM.start(LED,0,1000)
#number of times the button been pushed
#initial number of button
BP=0

while True:
    if GPIO.input(button1):
        BP=BP+1 #Button 1 is up
        print "Light up button was pressed"
    if GPIO.input(button2):
        BP=BP-1 #Button 1 is down
        print "Light down button was pressed"
    if BP>10:
        BP=10
    if BP<0:
        BP=0
    #DutyCycle=C^(BP)-B
    #tenth root of 101 = 1.5864
    DutyCycle=1.5864**(BP)-1
    PWM.set_duty_cycle(LED,DutyCycle)
    time.sleep(.2)
