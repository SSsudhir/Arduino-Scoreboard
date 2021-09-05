def gameScoreFormat(index, game, teams, valueLengths):
    scoreString = f'{teams[2*index]}:' # Team 1 Abbreviation
    scoreString += (5-valueLengths[0])*' ' # Spaces to align Team 1 and 2 scores (abbreviations can be 2 to 4 chars)
    scoreString += f'{game[teams[2*index]]}' # Team 1 Score
    scoreString += (8-valueLengths[2])*' ' # Spaces to align the current quarter with the end of the LCD
    scoreString += 'Q' + str(game['gameQuarter']) # Display current quarter
    scoreString += f'\{teams[2*index+1]}:' # Move to next line and display team 2 Abbreviation
    scoreString += (5-valueLengths[1])*' ' # Spaces to align Team 1 and 2 scores (abbreviations can be 2 to 4 chars)
    scoreString += f'{game[teams[2*index+1]]}' # Team 2 Score
    scoreString += (10-valueLengths[3]-valueLengths[4])*' ' # Spaces to align the game clock with the end of the LCD
    scoreString += str(game['gameClock']) # Display the game clock

    return scoreString

def playerStatFormat(game, index):
    # If game has not begun, do not format string as it is empty
    if str(game['playerName' + f'{index}']) == '':
        return ''


    playerString = str(game['playerName' + f'{index}'])

    playersStatLine = str(game['bestPlayerStats' + f'{index}'])
    playersStatLine = playersStatLine.replace(' ', '')
    playersStatLine = playersStatLine.replace('PTS', 'P')
    playersStatLine = playersStatLine.replace('REB', 'R')
    playersStatLine = playersStatLine.replace('AST', 'A')
    playersStatLine = playersStatLine.replace('BLK', 'B')
    playersStatLine = playersStatLine.replace('STL', 'S')
    playerString += f'\{playersStatLine}'

    return playerString