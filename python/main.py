import time
from time import sleep
import ESPNWebScraping
import Arduino
import StringFormatter

while True:
    try:
        runTime = int(input('How long would you like this program to run (in minutes)? '))
        break
    except:
        print('Error, try again! Make sure you enter a whole number like 1,2,20 etc.')


sport = 'nba' # Choose nba, nfl or mlb
obj = ESPNWebScraping.ESPNWebScraping("https://www.espn.com/" + sport + "/scoreboard/_/date/20190322")
arduino = Arduino.Arduino('/dev/cu.usbmodem1101') # Change Arduino Port to reflect your own

t_end = time.time() + runTime * 60
time.sleep(2) # Allow time for arduino to be created and initialized

print('Starting scoreboard! Type the keys control + c at anytime to stop the scoreboard')

while time.time() < t_end: # Run program till the user requested time expires
    teams = obj.getTeamPlayingToday()
    games = obj.getGameData()

    minuteTimer = time.time() + 60 

    while time.time() < minuteTimer: # Refresh the score every minute
        for index, game in enumerate(games):

            firstTeamLen = len(teams[2*index])
            secondTeamLen = len(teams[2*index+1])
            firstTeamScoreLen = len(game[teams[2*index]])
            secondTeamScoreLen = len(game[teams[2*index+1]])
            gameClockLen = len(game['gameClock'])

            if game['gameQuarter'] == 0:
                print("This is the game clock data type: {}".format(type(game['gameClock'])))

            displayString = StringFormatter.gameScoreFormat(index, game, teams, [firstTeamLen, secondTeamLen, firstTeamScoreLen, secondTeamScoreLen,gameClockLen])
            arduino.display(displayString)

            displayString = StringFormatter.playerStatFormat(game, 0)
            arduino.display(displayString)

            displayString = StringFormatter.playerStatFormat(game, 1)
            arduino.display(displayString)

    arduino.updatingScoreAnimation() # Play animation reflecting an update is ongoing

arduino.display('  Program Time  \     Expired    ')
arduino.close()


