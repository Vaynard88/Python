#!/usr/bin/env python3
########################################################################
# Filename    : Blink.py
# Description : Basic usage of GPIO. Let led blink.
# auther      : www.freenove.com
# modification: 2019/12/28
########################################################################
import RPi.GPIO as GPIO
import time

ledPin = 11    # define ledPin
word = str(input("Enter the morse code message you would like to send"))
word = word.replace(' ', '_')
def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, GPIO.LOW)
    print ('using pin%d'%ledPin)

def loop():
    while True:
        for letter in word:
            if letter == "_":
                time.sleep(.25)
            elif letter == "a":
                GPIO.output(ledPin, GPIO.HIGH)
                print ('led turned on >>>')
                time.sleep(.25)
                GPIO.output(ledPin, GPIO.LOW)
                print ('led turned off <<<')
                time.sleep(.25)
                GPIO.output(ledPin, GPIO.HIGH)
                print ('led turned on >>>')
                time.sleep(.50)
                GPIO.output(ledPin, GPIO.LOW)
                print ('led turned off <<<')
                time.sleep(.25)
            elif letter == "b":
                GPIO.output(ledPin, GPIO.HIGH)
                print ('led turned on >>>')
                time.sleep(.50)
                GPIO.output(ledPin, GPIO.LOW)
                print ('led turned off <<<')
                time.sleep(.25)
                GPIO.output(ledPin, GPIO.HIGH)
                print ('led turned on >>>')
                time.sleep(.25)
                GPIO.output(ledPin, GPIO.LOW)
                print ('led turned off <<<')
                time.sleep(.25)
                GPIO.output(ledPin, GPIO.HIGH)
                print ('led turned on >>>')
                time.sleep(.25)
                GPIO.output(ledPin, GPIO.LOW)
                print ('led turned off <<<')
                time.sleep(.25)
            elif letter == "c":
                GPIO.output(ledPin, GPIO.HIGH)
                print ('led turned on >>>')
                time.sleep(.50)
                GPIO.output(ledPin, GPIO.LOW)
                print ('led turned off <<<')
                time.sleep(.25)
                GPIO.output(ledPin, GPIO.HIGH)
                print ('led turned on >>>')
                time.sleep(.25)
                GPIO.output(ledPin, GPIO.LOW)
                print ('led turned off <<<')
                time.sleep(.25)
                GPIO.output(ledPin, GPIO.HIGH)
                print ('led turned on >>>')
                time.sleep(.50)
                GPIO.output(ledPin, GPIO.LOW)
                print ('led turned off <<<')
                time.sleep(.25)
                GPIO.output(ledPin, GPIO.HIGH)
                print ('led turned on >>>')
                time.sleep(.25)
                GPIO.output(ledPin, GPIO.LOW)
                print ('led turned off <<<')
                time.sleep(.25)
            elif letter == "d":
                GPIO.output(ledPin, GPIO.HIGH)
                print ('led turned on >>>')
                time.sleep(.50)
                GPIO.output(ledPin, GPIO.LOW)
                print ('led turned off <<<')
                time.sleep(.25)
                GPIO.output(ledPin, GPIO.HIGH)
                print ('led turned on >>>')
                time.sleep(.25)
                GPIO.output(ledPin, GPIO.LOW)
                print ('led turned off <<<')
                time.sleep(.25)
                GPIO.output(ledPin, GPIO.HIGH)
                print ('led turned on >>>')
                time.sleep(.25)
                GPIO.output(ledPin, GPIO.LOW)
                print ('led turned off <<<')
                time.sleep(.25)


        

def destroy():
    GPIO.cleanup()                      # Release all GPIO

if __name__ == '__main__':    # Program entrance
    print ('Program is starting ... \n')
    setup()
    try:
        loop()
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy()

