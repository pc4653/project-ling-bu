#!/usr/bin/env python
import freenect
import cv2
import socket
import signal
import serial
import time

light = 0
last_time = 0
ser = serial.Serial('/dev/ttyACM0',9600,timeout=5)
keep_running = True
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345               # Reserve a port for your service.
s.bind(('', port))        # Bind to the port
s.listen(5) 
conn, addr = s.accept()   
print 'Got connection from', addr


def body(dev, ctx):
    global light
    global last_time


    if not keep_running:
	conn.close()
	s.shutdown(socket.SHUT_RDWR)
	s.close()
	print 'socket shutting down'
        raise freenect.Kill

    if time.time() - last_time < 1:
        return
    last_time = time.time()

    freenect.set_led(dev, light) 
    
def display_rgb(dev, data, timestamp):
    global keep_running
    global light


    dataString = data.tostring()
    conn.send(dataString)
    try:
	transmit = conn.recv(10)
	output = int(transmit)
    	if output == 1:
		print 'detecting mode'
		light = 3
    	else:
		print output
		light = 1
	ser.write(transmit)
    except ValueError:
	pass	#this is to catch empty space when in tracking mode, necessary for blocking mode
	






def handler(signum, frame):
    """Sets up the kill handler, catches SIGINT"""
    global keep_running
    keep_running = False



signal.signal(signal.SIGINT, handler)
freenect.runloop(video=display_rgb,
                 body=body)  