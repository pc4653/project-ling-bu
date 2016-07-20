#!/usr/bin/env python
import freenect
import cv2
import time
import frame_convert2

cv2.namedWindow('RGB')
keep_running = True
last_time = 0
tilt = 0
light = 0


def body(dev, ctx):
    global last_time
    global tilt
    global light
    if not keep_running:
        raise freenect.Kill
 
    if tilt == 30:
        return

    if time.time() - last_time < 3:
        return
    last_time = time.time()
    led = light
    freenect.set_led(dev, led)
    freenect.set_tilt_degs(dev, tilt)
    print('led[%d] tilt[%d] accel[%s]' % (led, tilt, freenect.get_accel(dev)))
    
def display_rgb(dev, data, timestamp):
    global keep_running
    global tilt
    global light
    cv2.imshow('RGB', frame_convert2.video_cv(data))
    c = cv2.waitKey(10)
    if 'q' == chr(c & 255):
        keep_running = False
  
    if 's' == chr(c & 255):
	cv2.imwrite("saved.jpg", frame_convert2.video_cv(data))
    if 'u' == chr(c & 255):
	tilt = 25
    if 'd' == chr(c & 255):
        tilt = 5
    if '1' == chr(c & 255):
        light = 1
    if '2' == chr(c & 255):
        light = 2
    if '3' == chr(c & 255):
        light = 3


print('Press q in window to stop')
print('Press s in window to save a camera shot')

freenect.runloop(video=display_rgb,
                 body=body)
