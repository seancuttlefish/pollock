# Pollock Drawing Robot MK2
# Version 0.0.1
# Interact Digital Arts
# 21st August 2021
# Right motor on pins 6,7,9,10 (display off)
# Left motor on pins 13,14,15,16
# Servo on pin 4 (display off)
# Ultrasonic Sensor on pin 8
# https://www.interactdigitalarts.uk

from microbit import *

display.show(Image.HAPPY)
sleep(1000)

def forward(steps):
    pause = 5
    display.off()
    # Left
    pin13.write_digital(1)
    pin14.write_digital(0)
    pin15.write_digital(0)
    pin16.write_digital(1)
    # Right
    pin6.write_digital(1)
    pin7.write_digital(0)
    pin9.write_digital(0)
    pin10.write_digital(1)
    sleep(pause)
    # Left
    pin13.write_digital(0)
    pin14.write_digital(0)
    pin15.write_digital(1)
    pin16.write_digital(1)
    # Right
    pin6.write_digital(0)
    pin7.write_digital(0)
    pin9.write_digital(1)
    pin10.write_digital(1)
    sleep(pause)
    # Left
    pin13.write_digital(0)
    pin14.write_digital(1)
    pin15.write_digital(1)
    pin16.write_digital(0)
    # Right
    pin6.write_digital(0)
    pin7.write_digital(1)
    pin9.write_digital(1)
    pin10.write_digital(0)
    sleep(pause)
    # Left
    pin13.write_digital(1)
    pin14.write_digital(1)
    pin15.write_digital(0)
    pin16.write_digital(0)
    # Right
    pin6.write_digital(1)
    pin7.write_digital(1)
    pin9.write_digital(0)
    pin10.write_digital(0)
    sleep(pause)
    display.on()

# def backward(steps):
# def left(degrees):
# def right(degrees):
# def penup:
# def pendown:

while True:
    forward(10)
