#!/usr/bin/env python
import freenect
import cv2
import socket
import signal


faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
keep_running = True
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345               # Reserve a port for your service.
s.bind(('', port))        # Bind to the port
s.listen(5) 
conn, addr = s.accept()   
print 'Got connection from', addr


def body(dev, ctx):
    if not keep_running:
	conn.close()
        raise freenect.Kill
 
    
def display_rgb(dev, data, timestamp):
    global keep_running

    gray = cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
       gray,
       scaleFactor=1.3,
       minNeighbors=5,
       minSize=(30, 30),
       flags = cv2.CASCADE_SCALE_IMAGE
    )
    #print "found {0} face(s)".format(len(faces))
    for (x, y, w, h) in faces:
    	data = cv2.rectangle(data, (x, y), (x+w, y+h), (0, 255, 0), 2)

    dataString = data.tostring()
    conn.send(dataString)
    c = cv2.waitKey(10)
    if 'q' == chr(c & 255):
        keep_running = False
    
def handler(signum, frame):
    """Sets up the kill handler, catches SIGINT"""
    global keep_running
    keep_running = False



signal.signal(signal.SIGINT, handler)
freenect.runloop(video=display_rgb,
                 body=body)