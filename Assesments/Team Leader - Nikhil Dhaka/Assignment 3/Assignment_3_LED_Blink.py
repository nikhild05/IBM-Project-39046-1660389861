# Python code for LED blinking using RASPBERRY Pi

import sys
import time
import RPi.GPIO as GPIO             #importing GPIO library
LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
while True:
    GPIO.output(LED_PIN, GPIO.HIGH) #turning ON LED
    time.sleep(0.5)                 #waiting for 0.5 seconds
    GPIO.output(LED_PIN, GPIO.LOW)  #turning OFF LED
    time.sleep(0.5)                 #waiting for 0.5 seconds
GPIO.cleanup()