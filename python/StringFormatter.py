def stringFormatter(index, game, teams, valueLengths):
		scoreString = f'{teams[2*index]}:'
		scoreString += (5-valueLengths[0])*' '
		scoreString += f'{game[teams[2*index]]}'
		scoreString += (8-valueLengths[2])*' '
		scoreString += 'Q' + str(game['gameQuarter'])
		scoreString += f'\{teams[2*index+1]}:'
		scoreString += (5-valueLengths[1])*' '
		scoreString += f'{game[teams[2*index+1]]}'
		scoreString += (10-valueLengths[3]-valueLengths[4])*' '
		scoreString += str(game['gameClock'])

		return scoreString
