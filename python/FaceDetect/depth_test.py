#!/usr/bin/env python
import freenect
import cv2
import frame_convert2
import sys
import time
import math
import serial
from time import sleep

ser = serial.Serial('/dev/ttyACM0',9600,timeout=5)
cv2.namedWindow('RGB')
keep_running = True
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
light = 0
tilt = 15
search = False
increment = True
last_time = 0
distance = 2047
faces = 0
#timeout = 3;

def body(dev, ctx):
    global tilt
    global light
    global increment
    global last_time
#    global timeout
    if not keep_running:
        raise freenect.Kill

    if time.time() - last_time < 3:
        return
    last_time = time.time()
    
    if tilt >= 30:
	increment = False
    if tilt <= 20:
	increment = True
    
    led = light
    freenect.set_led(dev, led)
    if search:
	if increment:
		tilt = tilt + 5
	else:
		tilt = tilt - 5	
	
        freenect.set_tilt_degs(dev, tilt)
#	if timeout > 1:
#		timeout = timeout/2;
#    else:
#	timeout = timeout + 2; 
    #print('led[%d] tilt[%d] accel[%s]' % (led, tilt, freenect.get_accel(dev)))


def display_depth(dev, data, timestamp):
    global keep_running
    global search
    global faces
    global distance
    count = 0


    if not search:
	face_x_center = faces[0][0] + faces[0][2]/2
	face_y_center = faces[0][1] + faces[0][3]/2
	while data[face_x_center][face_y_center + count] == 2047:
	  if face_y_center + count < 481:
	    count = count + 1
	if face_y_center + count < 481:
		distance = data[face_x_center][face_y_center + count]

		distance = math.tan((distance/2842.5) + 1.1863)*0.1236
		print round(distance,2)


def display_rgb(dev, data, timestamp):
    global keep_running
    global faceCascade
    global light
    global tilt
    global search
    global faces
    global ser
    global last_time
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

    print "found {0} face(s)".format(len(faces))
    if len(faces) > 0:
	search = False
	light = 1
    	face_x_center = faces[0][0] + faces[0][2]/2
	face_y_center = faces[0][1] + faces[0][3]/2
    	diff = face_x_center - camera_x_center
#	print diff
    	if diff > 32:
		print "face on the right side, turn right!"
    	elif diff < -32:
		print "face on the left side, turn left!"
    	else :
		print "face straight ahead"
    else:
	print "no face"
	diff = 640
        search = True
	light = 3
    

    print diff
    ser.write(str(diff-641)) 


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

freenect.runloop(depth=display_depth,
		 video=display_rgb,
                 body=body)


#backlog
#start_x_ind = faces[0][0] + faces[0][2]/4
#end_x_ind = faces[0][0] + 3*faces[0][2]/4
#start_y_ind = faces[0][1] + faces[0][3]/4
#end_y_ind = faces[0][1] + 3*faces[0][3]/4    
#for x in range (0, end_x_ind - start_x_ind):
#    for y in range (0, end_y_ind - start_y_ind):
#	if data[x][y] != 2047:
#		total = total + data[start_x_ind+x][start_y_ind+y]
#		count = count + 1
#distance = total/count

    #if 'u' == chr(c & 255):
    # 	 tilt = 25
    #if 'd' == chr(c & 255):
    #    tilt = 5
    #if '1' == chr(c & 255):
    #    light = 1
    #if '2' == chr(c & 255):
    #    light = 2
    #if '3' == chr(c & 255):
    #    light = 3
