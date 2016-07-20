#!/usr/bin/env python
import freenect
import cv2
import frame_convert2
import math

keep_running = True
cv2.namedWindow('depth')

def display_depth(dev, data, timestamp):
    global keep_running
#distance = 0.1236 * tan(rawDisparity / 2842.5 + 1.1863)
    print data[320][240]
    if data[320][240] < 2047:
	distance = math.tan((data[320][240]/2842.5) + 1.1863)*0.1236
#	distance = distance + 1.1863
#	distance = math.tan(distance)
#	distance = 0.1236*distance
    else:
	distance = 2047
    print distance
    if cv2.waitKey(10) == 27:
        keep_running = False


def body(*args):
    if not keep_running:
        raise freenect.Kill


print('Press ESC in window to stop')
freenect.runloop(depth=display_depth,
                 body=body)
