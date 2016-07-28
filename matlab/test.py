#!/usr/bin/python           # This is server.py file
import socket               # Import socket module
import cv2

data_depth = cv2.imread('saved1.jpg')
data_image = cv2.imread('frame.jpg')
dataString_depth = data_depth.tostring()
dataString_image = data_image.tostring()
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345               # Reserve a port for your service.
s.bind(('', port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.


c, addr = s.accept()     # Establish connection with client.
print 'Got connection from', addr
c.send(dataString_depth)
c.send(dataString_image)
c.close()                # Close the connection


s.shutdown(socket.SHUT_RDWR)
s.close()
print 'socket shutting down' 