import serial
import time
import sys
from time import sleep

ser = serial.Serial('/dev/ttyACM0',9600,timeout=5)
print sys.argv[1]
ser.write(sys.argv[1])
ser.write('EOF')
num = 200
ser.write(str(num))
