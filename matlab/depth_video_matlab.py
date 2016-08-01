#!/usr/bin/env python
import freenect
import cv2
import socket
import signal


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
	s.shutdown(socket.SHUT_RDWR)
	s.close()
	print 'socket shutting down'
        raise freenect.Kill
 
def display_depth(dev, data, timestamp):
    global keep_running
    dataString = data.tostring()
    conn.send(dataString)


    
def handler(signum, frame):
    """Sets up the kill handler, catches SIGINT"""
    global keep_running
    keep_running = False



signal.signal(signal.SIGINT, handler)
freenect.runloop(depth=display_depth,
                 body=body)