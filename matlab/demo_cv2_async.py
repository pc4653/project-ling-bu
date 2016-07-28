#!/usr/bin/env python
import freenect
import cv2
import frame_convert2

cv2.namedWindow('Depth')
keep_running = True


def display_depth(dev, data, timestamp):
    global keep_running
    cv2.imshow('Depth', frame_convert2.pretty_depth_cv(data))
    c = cv2.waitKey(10)
    if 'q' == chr(c & 255):
        keep_running = False
  
    if 's' == chr(c & 255):
	cv2.imwrite("saved1.jpg", data)



def body(*args):
    if not keep_running:
        raise freenect.Kill

print('Press q in window to stop')
print('Press s in window to save a camera shot')
freenect.runloop(depth=display_depth,
                 body=body)
