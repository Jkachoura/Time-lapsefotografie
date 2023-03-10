# Test code for sending serial commands to ZOE, this command will reboot the ZOE cell imager.
import serial
import time
import sys

def serial_ports():
    ''' Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    '''
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

capture = [1981,1973]



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

touchButt(capture)
