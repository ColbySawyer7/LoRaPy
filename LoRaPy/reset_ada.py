#!/usr/bin/env python
import RPi.GPIO as GPIO  
import time


def reset():
    RESET = 25
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RESET, GPIO.OUT)
    GPIO.output(RESET, GPIO.HIGH)
    time.sleep(.100)
    GPIO.output(RESET, GPIO.LOW)
    GPIO.cleanup()

    print("reset adafruit bonnet.")
