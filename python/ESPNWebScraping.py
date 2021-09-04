import bs4
from bs4 import BeautifulSoup
import requests
import json

class ESPNWebScraping():
	def __init__(self, url, teams = []):
		self.teams = teams
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

		s = str(soup.select('script')[13])
		finalString = s[38:-10]
		finalString = finalString.replace(";window.espn.scoreboardSettings = ", "")
		endString = finalString.find('{"useStatic":')
		tempString = finalString[:endString]

		finalJSON = json.loads(tempString)

		self.gameData = []

		for index, game in enumerate(finalJSON['events']):
			self.gameData.append([])

			for team in game['competitions'][0]['competitors']:
				abbrev = team['team']['abbreviation']
				score = team['score']

				if type(self.gameData[index]) is not dict:
					self.gameData[index] = {}

				self.gameData[index][abbrev] = score

			self.gameData[index]['gameQuarter'] = game['status']['period']
			self.gameData[index]['gameClock'] = game['status']['displayClock']
