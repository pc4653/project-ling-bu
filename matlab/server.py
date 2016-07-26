#!/usr/bin/python           # This is server.py file
import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345               # Reserve a port for your service.
s.bind(('', port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
s.setblocking(0)
while True:
   try:
	c, addr = s.accept()     # Establish connection with client.
	print 'Got connection from', addr
	while True:
		try:
   			print c.recv(1024)
			c.close()                # Close the connection
		except socket.error:
			pass
			#print 'no data yet'
   except socket.error:
	pass
	#print 'no connection yet'


 