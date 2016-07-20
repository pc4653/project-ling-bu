#!/usr/bin/env python
import freenect
import cv2
import frame_convert2
import sys


cv2.namedWindow('RGB')
keep_running = True
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


def body(dev, ctx):
    if not keep_running:
        raise freenect.Kill
 
    
def display_rgb(dev, data, timestamp):
    global keep_running
    global faceCascade
    camera_x_center = 320

    image = frame_convert2.video_cv(data)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
       gray,
       scaleFactor=1.1,
       minNeighbors=5,
       minSize=(30, 30),
       flags = cv2.CASCADE_SCALE_IMAGE
    )

    print "{0}".format(len(faces))
    if len(faces) > 0:
    	face_x_center = faces[0][0] + faces[0][2]/2
	face_y_center = faces[0][1] + faces[0][3]/2
    	diff = face_x_center - camera_x_center
	print diff
    	if diff > 32:
		print "face on the right side, turn right!"
    	elif diff < -32:
		print "face on the left side, turn left!"
    	else :
		print "face straight ahead"
    else:
	print "no face"
	diff = 640
    c = cv2.waitKey(10)
    if 'q' == chr(c & 255):
        keep_running = False
    if 's' == chr(c & 255):
	cv2.imwrite('detected.jpg', image)
	image = cv2.imread('detected.jpg')
	for (x, y, w, h) in faces:
    		cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
	cv2.imwrite('detected.jpg', image)
 
    


print('Press q in window to stop')
print('Press s in window to save a camera shot')

freenect.runloop(video=display_rgb,
                 body=body)
