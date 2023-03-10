# Test code for sending serial commands to ZOE, this command will reboot the ZOE cell imager.
import serial
import time
import sys
import datetime

capture = [1981,1973]
export = [1982,1974]
live = [1941,435]
wLed = [87, 762]
bLed = [88, 1041]
gLed = [89, 1251]
rLed = [90, 1503]

captureInterval= 30
timelapseDuration = 3 * captureInterval
totalpictures = (timelapseDuration / captureInterval) * 2 + 2
takenpictures = 0

WLED = False
BLED = True
GLED = False
RLED = True

def serial_ports():
    ''' Lists serial port names

        :returns:
            A list of the serial ports available on the system
    '''
    ports = list(serial.tools.list_ports.comports())
    result = []
    for port in ports:
        result.append(port.device)
    return result

def touchButt(input):
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

if __name__ == "__main__":
    comPort = serial_ports()[0]
    ser = serial.Serial(comPort, 115200, timeout=1)
    # timelapse with 2 leds.
    # TODO its not working properly yet cause of the maximum events the shell can take need to find a solution for this
    while takenpictures <= totalpictures:
        if WLED:
            ct = datetime.datetime.now()
            print("Taking WLED picture " + str(takenpictures) + " " + str(ct))
            touchButt(live)
            touchButt(wLed)
            touchButt(capture)
            time.sleep(10)
            takenpictures += 1
        if BLED:
            ct = datetime.datetime.now()
            print("Taking BLED picture " + str(takenpictures) + " " + str(ct))
            touchButt(live)
            touchButt(bLed)
            touchButt(capture)
            time.sleep(10)
            takenpictures += 1
        if GLED:
            ct = datetime.datetime.now()
            print("Taking GLED picture " + str(takenpictures) + " " + str(ct))
            touchButt(live)
            touchButt(gLed)
            touchButt(capture)
            time.sleep(10)
            takenpictures += 1
        if RLED:
            ct = datetime.datetime.now()
            print("Taking RLED picture " + str(takenpictures) + " " + str(ct))
            touchButt(live)
            touchButt(rLed)
            touchButt(capture)
            time.sleep(10)
            takenpictures += 1
        if takenpictures != totalpictures:
            time.sleep(captureInterval)
    print("Done with timelapse")