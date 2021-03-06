#!/usr/bin/env python
import freenect
import cv2
import frame_convert2
import signal

cv2.namedWindow('RGB')
keep_running = True

def body(dev, ctx):
    if not keep_running:
        raise freenect.Kill
 
    
def display_rgb(dev, data, timestamp):
    global keep_running
    cv2.imshow('RGB', frame_convert2.video_cv(data))
    c = cv2.waitKey(10)
    if 'q' == chr(c & 255):
        keep_running = False
  
    if 's' == chr(c & 255):
	cv2.imwrite("saved1.jpg", frame_convert2.video_cv(data))
    
def handler(signum, frame):
    """Sets up the kill handler, catches SIGINT"""
    global keep_running
    keep_running = False

print('Press q in window to stop')
print('Press s in window to save a camera shot')
signal.signal(signal.SIGINT, handler)
freenect.runloop(video=display_rgb,
                 body=body)
