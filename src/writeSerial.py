# Test code for sending serial commands to ZOE, this command will reboot the ZOE cell imager.
import serial
import time
import serial.tools.list_ports
from itertools import compress

RLED = True
GLED = False
BLED = True
WLED = False

# Button coordinates
capture =   [1981, 1973]
export  =   [1982, 1974]
live    =   [1941, 435]
wLed    =   [87, 762]
bLed    =   [88, 1041]
gLed    =   [89, 1251]
rLed    =   [90, 1503]

# Microscope reboot time
rebootTime = 20

def serial_ports():
    """List serial port names

        returns:
            A list of the serial ports available on the system
    """
    ports = list(serial.tools.list_ports.comports())
    result = []
    for port in ports:
        result.append(port.device)
    return result

def touchButton(input):
    """Simulate touch event

    Args:
        input: (x, y) screen coordinate
    """

    xString = f'sendevent /dev/input/event1 3 53 {str(input[0])}\r\n'
    yString = f'sendevent /dev/input/event1 3 54 {str(input[1])}\r\n'

    ser.write(b'sendevent /dev/input/event1 3 57 0\r\n')
    ser.write(bytes(xString, encoding= 'utf-8'))
    ser.write(bytes(yString, encoding= 'utf-8'))
    ser.write(b'sendevent /dev/input/event1 0 0 0\r\n')
    time.sleep(0.1)
    ser.write(b'sendevent /dev/input/event1 3 57 -1\r\n')
    ser.write(b'sendevent /dev/input/event1 0 2 0\r\n')
    ser.write(b'sendevent /dev/input/event1 0 0 0\r\n')
    time.sleep(2)

def takeCapture(led):
    """Simulate events to take capture

    Args:
        led: capture colour
    """

    touchButton(live)
    touchButton(led)
    touchButton(capture)
    time.sleep(10)

def reboot():
    ser.write(b'reboot\r\n')
    time.sleep(rebootTime)

def makeTimeLapse(cycleAmount, cycleInterval, ledColours):
    """Make a time-lapse based on given arguments

    Args:
        cycleAmount: amount of cycles in time-lapse
        cycleInterval: time between cycles
        ledColours: list of led colours to make the captures
    """

    takenCycles = 0
    takenPictures = 0
    while takenCycles < cycleAmount:
        for led in ledColours:
            takeCapture(led)
        takenCycles += 1
        takenPictures += len(ledColours)
        reboot()
        time.sleep(cycleInterval - rebootTime)
    print("Done with timelapse, total pictures taken: " + str(takenPictures))
    reboot()

if __name__ == "__main__":
    comPort = serial_ports()[0]
    ser = serial.Serial(comPort, 115200, timeout=1)
    makeTimeLapse(2, 30, list(compress([rLed, gLed, bLed, wLed], [RLED, GLED, BLED, WLED])))