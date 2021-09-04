import serial
import time

class Arduino(object):
    def __init__(self, port):
        self.s = serial.Serial(port, 9800, timeout=1)

    def display(self, string):
        if string == '':
            return
        self.s.write(str.encode(string))
        time.sleep(4)

    def updatingScoreAnimation(self):
        self.s.write(str.encode('~'))
        self.s.write(str.encode('    Updating \     Scores'))
        time.sleep(3)
        self.s.write(str.encode('~'))

    def close(self):
        self.s.close()
