from generator import generateBoard
from index import goalIndex, parseGoalPool, parseOptions
from random import choice, choices
import os
import argparse

options = parseOptions()

def main():

    parser = argparse.ArgumentParser(description='Generate Minecraft Lockout boards with the Truff1e lockout generator.')

    parser.add_argument('--boardtype', '-b',
                        type=str,
                        default='balanced',
                        help='Set generator mode to balanced (default) or custom')

    parser.add_argument('customgoals',
                        nargs='*',
                        help='Set a list of goal ids for custom board.')

    parser.add_argument('--boardsize', '-s',
                        type=int,
                        default='5',
                        help='Set board size (1-10). Larger sizes may be unstable.')

    parser.add_argument('--pool', '-p',
                        type=str,
                        default='Lockout',
                        help='Set a goal pool to draw from when generating the board. See options with -P.')

    parser.add_argument('--listpools', '-P',
                        action='store_true',
                        help='List all loaded goal pools.')

    parser.add_argument('--difficulty', '-d',
                        type=str,
                        default='1-5',
                        help='Set the difficulty range (int-int). Min 1, max 10.')

    args = parser.parse_args()

    if args.listpools:
        goalPools = os.listdir('goal_pools')
        for pool in goalPools:
            if pool[-5:] == '.json':
                print(' >', pool[:-5])
    else:
        if args.boardtype == 'custom':
            generateCustomboard(args.customgoals)
        if args.boardtype == 'balanced':
            generateBalancedBoard(args.boardsize, (float(args.difficulty.split('-')[0]), None, float(args.difficulty.split('-')[1])), args.pool)

    exit()



def getid(goal):
    for i in goalIndex:
        if goalIndex[i][0].lower() == goal.lower():
            print(f'>> {goal} has a goal ID of: {i}')
            return i
    print(f"Goal Lookup Error: {goal} is not a valid goal id")
    return "Goal not found."


def getrandomgoal():
    return choice(list(goalIndex))


def translate(goal_id):
    if str(goal_id).upper() in goalIndex:
        print(f'>> {goal_id} has a goal name of: {goalIndex[str(goal_id)][0]}')
        return goalIndex[str(goal_id)][0]
    else:
        print(">> Goal not found.")
        return "Goal not found."


def checkExcludedGoals(newgoal, excluded):
    for goal in excluded:
        if newgoal == goal:
            return True
            # Goal is excluded
    return False
    # Goal is not excluded


def generateCustomboard(boardBlueprint: list):
    print(f'Generating Lockout Board')
    print(f'Type: Custom')
    print(f'Size: {int(len(boardBlueprint)**0.5)}')
    generateBoard(boardBlueprint, f'custom-s{int(len(boardBlueprint)**0.5)}')
    return boardBlueprint


def generateBalancedBoard(size: int, difficultySet: tuple, poolId, excluded=None):
    if excluded is None:
        excluded = []

    minDifficulty, difficultyWeights, maxDifficulty = difficultySet
    goalPool = parseGoalPool(poolId)

    print(f'Generating Lockout Board')
    print(f'Type: Balanced')
    print(f'Size: {size}')
    print(f'Difficulty: {difficultySet}')
    print(f'Pool: {poolId}')

    boardBlueprint = [] 
    for _ in range(size**2):
        if difficultyWeights != None:
            preferredDifficulty = choices(range(minDifficulty, maxDifficulty+1), weights=difficultyWeights, k=1)[0]
        else:
            preferredDifficulty = None

        newgoal = choice(goalPool)
        runs = 0
        while ((newgoal in boardBlueprint) or (goalIndex[newgoal][3] not in range(int(minDifficulty), int(maxDifficulty)+1)) 
                or (goalIndex[newgoal][3] != preferredDifficulty if preferredDifficulty != None else False)
                or checkExcludedGoals(newgoal, excluded)) or newgoal in boardBlueprint:
            newgoal = choice(goalPool)
            runs += 1
            if runs > 300:
                print(" > [Error] Failed to find compatible goal. Reverting to random non-duplicate.")
                break
        while newgoal in boardBlueprint:
            newgoal = choice(goalPool)

        boardBlueprint.append(newgoal)
        print(f' > Added {newgoal} ({goalIndex[newgoal][0]}) of difficulty {goalIndex[newgoal][3]}')

    generateBoard(boardBlueprint, f's{size}-d{minDifficulty}-{maxDifficulty}')
    return boardBlueprint


if __name__ == '__main__':
    print('---------------------------------------------------------------------')
    print(f'Truffle Minecraft Lockout - v{options['version']}')
    print(f'©2025 - Truffle Studios (GNU GPLv3)')
    print(f'Supports MC {options['mcVersion']} - Pass -h for help')
    print('---------------------------------------------------------------------')
    main()
