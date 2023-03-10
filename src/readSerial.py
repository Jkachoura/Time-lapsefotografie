# Testcode for reading the serial data coming from the ZOE cell imager

import serial
import time
import sys

def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


if __name__ == "__main__":
    comPort = serial_ports()[0]
    ser = serial.Serial(comPort, 115200, timeout=1)

    while True:
        line = ser.readline() 
        if line:
            print(line)
        time.sleep(0.01)