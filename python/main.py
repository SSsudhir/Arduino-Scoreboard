import time
from time import sleep
import ESPNWebScraping
import Arduino

while True:
	try:
		runTime = int(input('How long would you like this program to run (in minutes)? '))
		break
	except:
		print('Error, try again! Make sure you enter a whole number like 1,2,20 etc. and you enter either nba, mlb or nfl.')

sport = 'nba' # Choose nba, nfl or mlb
obj = ESPNWebScraping.ESPNWebScraping("https://www.espn.com/" + sport + "/scoreboard/_/date/20210423")
arduino = Arduino.Arduino('/dev/cu.usbmodem1101')
t_end = time.time() + runTime * 60
time.sleep(2) # Allow time for arduino to be created and initialized

print('Starting scoreboard! Type the keys control + c at anytime to stop the scoreboard')

while time.time() < t_end:
	teams = obj.getTeamPlayingToday()
	games = obj.getGameData()
    
	for index, game in enumerate(games):

		firstTeamLen = len(teams[2*index])
		secondTeamLen = len(teams[2*index+1])

		firstTeamScoreLen = len(game[teams[2*index]])
		secondTeamScoreLen = len(game[teams[2*index+1]])

		gameClockLen = len(game['gameClock'])

		scoreString = f'{teams[2*index]}:'
		scoreString += (5-firstTeamLen)*' '
		scoreString += f'{game[teams[2*index]]}'
		scoreString += (8-firstTeamScoreLen)*' '
		scoreString += 'Q' + str(game['gameQuarter'])
		scoreString += f'\{teams[2*index+1]}:'
		scoreString += (5-secondTeamLen)*' '
		scoreString += f'{game[teams[2*index+1]]}'
		scoreString += (10-secondTeamScoreLen-gameClockLen)*' '
		scoreString += str(game['gameClock'])

		arduino.display(scoreString)
		time.sleep(5)

	arduino.updatingScoreAnimation()
    
arduino.close()


