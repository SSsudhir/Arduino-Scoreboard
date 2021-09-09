import serial
import time

class Arduino(object):
    def __init__(self, port):
        self.s = serial.Serial(port, 9800, timeout=1)

    def display(self, string):
        # If string is empty, there is nothing to display, therefore return
        if string == '':
            return
        self.s.write(str.encode(string))
        time.sleep(4)

    def updatingScoreAnimation(self):
        # Animation reflecting a score update is in progress
        self.s.write(str.encode('~'))
        self.s.write(str.encode('    Updating \     Scores'))
        time.sleep(3)
        self.s.write(str.encode('~'))

    def turnOnLED(self):
        self.s.write(str.encode('!'))

    def turnOffLED(self):
        self.s.write(str.encode('$'))

    def close(self):
        self.s.close()
