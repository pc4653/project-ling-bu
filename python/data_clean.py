#!/usr/bin/env python
import freenect
import cv2
import frame_convert2

cv2.namedWindow('RGB')
keep_running = True

def body(dev, ctx):
    if not keep_running:
        raise freenect.Kill
 
    
def display_rgb(dev, data, timestamp):
    global keep_running
    print frame_convert2.video_cv(data)
    c = cv2.waitKey(10)
    if 'q' == chr(c & 255):
        keep_running = False
  
    if 's' == chr(c & 255):
	cv2.imwrite("saved1.jpg", frame_convert2.video_cv(data))
    


print('Press q in window to stop')
print('Press s in window to save a camera shot')

freenect.runloop(video=display_rgb,
                 body=body)
