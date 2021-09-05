import bs4
from bs4 import BeautifulSoup
import requests
import json

class ESPNWebScraping():
    def __init__(self, url):
        self.url = url
        self.gameData = []

    def getGameData(self):
        self.updateScore()
        return self.gameData

    def getTeamPlayingToday(self):
        self.updateScore()

        teamsPlayingToday = []

        for game in self.gameData:
            teamsPlayingToday += list(game.keys())[:2]

        return teamsPlayingToday
        
    def updateScore(self):
        result = requests.get(self.url)
        soup = bs4.BeautifulSoup(result.text, "lxml")

        # Extract only relevant data
        s = str(soup.select('script')[13])
        finalString = s[38:-10]
        finalString = finalString.replace(";window.espn.scoreboardSettings = ", "")
        endString = finalString.find('{"useStatic":')
        tempString = finalString[:endString]

        # Convert string to JSON Object
        finalJSON = json.loads(tempString)

        self.gameData = []

        # Iterate through every game that day
        for index, game in enumerate(finalJSON['events']):
            self.gameData.append([])
            bestPlayerName = []
            bestPlayerStats = []

            # Iterate through each team in the game
            for team in game['competitions'][0]['competitors']:
                abbrev = team['team']['abbreviation']
                score = team['score']

                try:
                    bestPlayerName.append(team['leaders'][3]['leaders'][0]['athlete']['shortName'])
                    bestPlayerStats.append(team['leaders'][3]['leaders'][0]['displayValue'])
                except:
                    bestPlayerName.append('')
                    bestPlayerStats.append('')

                if type(self.gameData[index]) is not dict:
                    self.gameData[index] = {}

                self.gameData[index][abbrev] = score


            self.gameData[index]['gameQuarter'] = game['status']['period']
            self.gameData[index]['gameClock'] = game['status']['displayClock']
            self.gameData[index]['playerName0'] = bestPlayerName[0]
            self.gameData[index]['playerName1'] = bestPlayerName[1]
            self.gameData[index]['bestPlayerStats0'] = bestPlayerStats[0]
            self.gameData[index]['bestPlayerStats1'] = bestPlayerStats[1]
