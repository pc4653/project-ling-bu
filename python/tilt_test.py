#!/usr/bin/env python
import freenect
import time
import random
import signal

keep_running = True
#last_time = 0

#LED encoding 0 is off, 1 is green, 2 is red, 3 is yellow, 4 is blink green, 5 is blink red and yellow
def body(dev, ctx):
    #global last_time
    if not keep_running:
        raise freenect.Kill

    #last_time = time.time()
    led = 1
    tilt = int(input("Enter a degree 0 - 30: "))
    #tilt = random.randint(0, 30)
    freenect.set_led(dev, led)
    freenect.set_tilt_degs(dev, tilt)
    print('led[%d] tilt[%d] accel[%s]' % (led, tilt, freenect.get_accel(dev)))


def handler(signum, frame):
    """Sets up the kill handler, catches SIGINT"""
    global keep_running
    keep_running = False
print('Press Ctrl-C in terminal to stop')
#signal.signal(signal.SIGINT, handler)
freenect.runloop(body=body)
