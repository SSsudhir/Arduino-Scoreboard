import serial
import time
from time import sleep
import ESPNWebScraping


obj = ESPNWebScraping.ESPNWebScraping()
s = serial.Serial('/dev/cu.usbmodem1101', 9800, timeout=1)
time.sleep(2)

while True:
	teams = obj.getTeamPlayingToday()
	games = obj.getGameData()
	s.write(str.encode(f'{teams[2]}: {games[1][teams[2]]}       \{teams[3]}: {games[1][teams[3]]}'))
	time.sleep(5)
	s.write(str.encode('~'))
	
# s.write(str.encode('TOR: 105      Q4\GSW: 104      1"'))
# time.sleep(5)
# s.write(str.encode('~'))
# s.write(str.encode('TOR: 105      Q4\GSW: 106      1"'))
# time.sleep(5)
# s.write(str.encode('~'))
# s.write(str.encode('TOR: 107      Q4\GSW: 106      1"'))
# time.sleep(5)
# s.write(str.encode('~'))
# s.write(str.encode('  TORONTO Wins\     107-106'))
    
s.close()


