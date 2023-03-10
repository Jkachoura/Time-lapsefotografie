# Testcode for reading the serial data coming from the ZOE cell imager

from serial.tools.list_ports import comports
import serial
import time

if __name__ == "__main__":
    """ Lists serial port names
        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    ports = [port.device for port in comports()]
    ser = serial.Serial(ports[0], 115200, timeout=1)

    while True:
        print(ser.readline().decode().strip())
        time.sleep(0.01)