#!/usr/bin/python           # This is server.py file
import socket               # Import socket module
import cv2

data = cv2.imread('frame.jpg')
dataString = data.tostring()
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345               # Reserve a port for your service.
s.bind(('', port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   c.send(dataString)
   c.close()                # Close the connection
