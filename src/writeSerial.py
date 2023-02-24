# Test code for sending serial commands to ZOE, this command will reboot the ZOE cell imager.
import serial

ser = serial.Serial('COM12', 115200, timeout=1)

ser.write(b'reboot\r\n')