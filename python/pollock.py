from microbit import *

pause = 5

while True:
    display.show(Image.HAPPY)
    pin13.write_digital(1)
    pin14.write_digital(0)
    pin15.write_digital(0)
    pin16.write_digital(1)
    sleep(pause)
    pin13.write_digital(0)
    pin14.write_digital(0)
    pin15.write_digital(1)
    pin16.write_digital(1)
    sleep(pause)
    pin13.write_digital(0)
    pin14.write_digital(1)
    pin15.write_digital(1)
    pin16.write_digital(0)
    sleep(pause)
    pin13.write_digital(1)
    pin14.write_digital(1)
    pin15.write_digital(0)
    pin16.write_digital(0)
    sleep(pause)
