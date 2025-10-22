from lockout import *
from index import exclusiveSets
from devtools import *


# global variables
gameVersion = '1.21.8'
disabledGoals = []



def main():
    boardType = input('Enter Board Type \n>>> ')

    if boardType == 'custom' or boardType == 'c':
        goals = input('Paste Goals \n>>> ')
        generateCustomboard(goals.strip(" ").split(','))
    elif boardType == 'balanced' or boardType == 'b':
        boardSize = input('Enter a Board Size\n>>> ')
        blackout = input('Enter for Lockout, anything for Blackout\n>>> ')
        minDiff = input('Minimum Difficulty\n>>> ')
        maxDiff = input('Maximum Difficulty\n>>> ')
        if blackout != '':
            generateBalancedBoard(int(boardSize), (float(minDiff), None, float(maxDiff)), ['all'])
        else:
            excluded = []
            for goal in exclusiveSets['opponent']:
                excluded.append(goal)
            generateBalancedBoard(int(boardSize), (float(minDiff), None, float(maxDiff)), ['all'], excluded=excluded)

    exit()


if __name__ == '__main__':
    print('======================================================')
    print('    ***  Truffle Lockout Generator v2.0 CLI  ***')
    print('               for MC 1.21.8-1.21.10')
    print('======================================================')
    main()
