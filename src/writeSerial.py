# Test code for sending serial commands to ZOE, this command will reboot the ZOE cell imager.
import serial
import time
import serial.tools.list_ports
from itertools import compress

RLED  = True
GLED  = False
BLED  = False
WLED  = False
MERGE = False

# Button coordinates
capture  =   [1981, 1973]
save     =   [1981, 1973]
export   =   [1982, 1974]
live     =   [1941, 435]
wLed     =   [87, 762]
bLed     =   [88, 1041]
gLed     =   [89, 1251]
rLed     =   [90, 1503]
select   =   [1458, 127]
merge    =   [1950, 849]
deselect =   [1782, 129]
gallery  =   [1950, 642]

# Microscope capture time
captureDelay = 15
# Microscope merge time
mergeDelay = 5
# Microscope save time
saveDelay = 5
# Microscope export time
exportDelay = 10
# Microscope sleep time
sleepTime = 1800
# Keep in track of lastLED for cycles with 1 LED
lastLED = wLed

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

    if input == "reboot":
        ser.write(b'reboot\r\n')
        return

    xString = f'sendevent /dev/input/event1 3 53 {str(input[0])}\r\n'
    yString = f'sendevent /dev/input/event1 3 54 {str(input[1])}\r\n'
    xString2 = f'sendevent /dev/input/event1 3 53 {str(input[0]+2)}\r\n'
    yString2 = f'sendevent /dev/input/event1 3 54 {str(input[1]+2)}\r\n'

    ser.write(b'sendevent /dev/input/event1 3 57 0\r\n')
    ser.write(bytes(xString, encoding= 'utf-8'))
    ser.write(bytes(yString, encoding= 'utf-8'))
    ser.write(b'sendevent /dev/input/event1 0 0 0\r\n')
    ser.write(bytes(xString2, encoding= 'utf-8'))
    ser.write(bytes(yString2, encoding= 'utf-8'))
    time.sleep(0.1)
    ser.write(b'sendevent /dev/input/event1 0 0 0\r\n')
    ser.write(b'sendevent /dev/input/event1 3 57 -1\r\n')
    ser.write(b'sendevent /dev/input/event1 0 0 0\r\n')

def takeCapture(led):
    """Simulate events to take capture

    Args:
        led: capture colour
    """

    global lastLED

    touchButton(live)
    # Touch wanted LED when last LED was different
    if not led == lastLED:
        touchButton(led)
    lastLED = led
    touchButton(capture)
    time.sleep(captureDelay)
    touchButton(select)
    touchButton(export)
    time.sleep(exportDelay)

def makeMerge():
    """ Merges selected images

    """

    touchButton(merge)
    time.sleep(mergeDelay)
    touchButton(save)
    time.sleep(saveDelay)
    touchButton(deselect)
    touchButton(export)

def makeTimeLapse(cycleAmount, cycleInterval, ledColours, merge):
    """Make a time-lapse based on given arguments

    Args:
        cycleAmount: amount of cycles in time-lapse
        cycleInterval: time between cycles
        ledColours: list of led colours to make the captures
    """

    takenCycles = 0
    takenPictures = 0
    madeMerges = 0
    # Loop through wanted cycles
    while takenCycles < cycleAmount:
        # Make capture of LED list
        for led in ledColours:
            takeCapture(led)
        if merge:
            makeMerge()
            madeMerges += 1
        takenCycles += 1
        takenPictures += len(ledColours)

        print("Cycle " + str(takenCycles) + " is done")
        # Prevent ZOE from turning off by emulating touch every sleeptime duration
        if cycleInterval > sleepTime:
            # Amount that sleeptime fits in cycle-interval
            touchAmount = int(cycleInterval / sleepTime)
            for i in range(touchAmount):
                time.sleep(sleepTime)
                touchButton(gallery)
            # Remainder
            time.sleep(cycleInterval - (touchAmount * sleepTime))
        else:
            time.sleep(cycleInterval)
    print("Done with timelapse, total pictures taken: " + str(takenPictures))
    print("Total merged pictures: " + str(madeMerges))

if __name__ == "__main__":
    comPort = serial_ports()[0]
    ser = serial.Serial(comPort, 115200, timeout=1)
    makeTimeLapse(3, 360, list(compress([rLed, gLed, bLed, wLed], [RLED, GLED, BLED, WLED])), True)