import serial
import time
from time import sleep
import ESPNWebScraping


obj = ESPNWebScraping.ESPNWebScraping("https://www.espn.com/nba/scoreboard")
s = serial.Serial('/dev/cu.usbmodem1101', 9800, timeout=1)
time.sleep(2)

while True:
	try:
		runTime = int(input('How long would you like this program to run (in minutes)? You can always control+c to exit as well: '))
		break
	except:
		print('Error, try again! Make sure you enter a whole number like 1,2,20 etc.')

t_end = time.time() + runTime * 60

while time.time() < t_end:
	teams = obj.getTeamPlayingToday()
	games = obj.getGameData()
    
	for index, game in enumerate(games):
		firstTeamLen = len(teams[2*index])
		secondTeamLen = len(teams[2*index+1])
		firstTeamScoreLen = len(game[teams[2*index]])
		secondTeamScoreLen = len(game[teams[2*index+1]])

		scoreString = f'{teams[2*index]}:'
		scoreString += (5-firstTeamLen)*' '
		scoreString += f'{game[teams[2*index]]}\{teams[2*index+1]}:'
		scoreString += (5-secondTeamLen)*' '
		scoreString += f'{game[teams[2*index+1]]}'

		s.write(str.encode(scoreString))
		time.sleep(5)

	s.write(str.encode('~'))
	# obj.updateScore()
    
s.close()


