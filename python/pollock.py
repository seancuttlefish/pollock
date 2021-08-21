# Pollock Drawing Robot
# pollock.py v0.0.1
# Interact Digital Arts
# 21st August 2021

from microbit import *

motor1 = [13, 14, 15, 16]
pause = 5

def forward(steps):
	motor1[0].write_digital(1)
	motor1[1].write_digital(0)
	motor1[2].write_digital(0)
	motor1[3].write_digital(1)
	sleep(pause)
	motor1[0].write_digital(0)
	motor1[1].write_digital(0)
	motor1[2].write_digital(1)
	motor1[3].write_digital(1)
	sleep(pause)
	motor1[0].write_digital(0)
	motor1[1].write_digital(1)
	motor1[2].write_digital(1)
	motor1[3].write_digital(0)
	sleep(pause)
	motor1[0].write_digital(1)
	motor1[1].write_digital(1)
	motor1[2].write_digital(0)
	motor1[3].write_digital(0)
	sleep(pause)

while True:
	forward(10)
