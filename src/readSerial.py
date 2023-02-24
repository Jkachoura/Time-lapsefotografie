# Testcode for reading the serial data coming from the ZOE cell imager

import serial
import time

ser = serial.Serial('COM12', 115200, timeout=1)

while True:
    line = ser.readline() 
    if line:
        print(line)
    time.sleep(0.01)