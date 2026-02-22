from index import *
from generator import generateBoard
from random import choice, choices
import os
import argparse


def main():

    parser = argparse.ArgumentParser(description='Generate Minecraft Lockout boards with the Truff1e lockout generator.')

    parser.add_argument('-b', '--boardtype',
                        type=str,
                        default='balanced',
                        help='Set generator mode to balanced (default) or custom')

    parser.add_argument('customgoals',
                        nargs='*',
                        help='Set a list of goal ids for custom board.')

    parser.add_argument('-s', '--boardsize',
                        type=int,
                        default=DEFAULT_SIZE,
                        help='Set board size (1-10). Larger sizes may be unstable.')

    parser.add_argument('-p', '--pool',
                        type=str,
                        default=DEFAULT_MODE,
                        help='Set a goal pool to draw from when generating the board. See options with -P.')

    parser.add_argument('-P', '--listpools',
                        action='store_true',
                        help='List all loaded goal pools.')

    parser.add_argument('-I', '--poolinfo',
                        help='Get information about a specific goal pool.')

    parser.add_argument('-d', '--difficulty',
                        type=str,
                        default=DEFAULT_DIFFICULTY,
                        help='Set the difficulty range (int-int). Min 1, max 10.')

    parser.add_argument('-v', '--version',
                        action='store_true',
                        help='Print version info, license & credits.')

    args = parser.parse_args()

    if args.version:
        print(dumpGeneratorInfo())
        exit()

    if args.listpools:
        goalPools = os.listdir('goal_pools')
        for pool in goalPools:
            if pool[-5:] == '.json':
                print(' >', pool[:-5])
    elif args.poolinfo:
        pool = args.poolinfo
        meta = getGoalPoolMeta(pool)
        if meta == None:
            print('Goal pool not found')
            return
        print(' > NAME:        ', meta['name'])
        print(' > DESCRIPTION: ', meta['description'])
        print(' > AUTHOR:      ', meta['author'])
        print(' > LAST_UPDATE: ', meta['last_updated'])
        print(' > VERSION:     ', meta['version'])
        print(' > DP_VERSION:  ', meta['dp_version'])
    else:
        if args.boardtype == 'custom':
            generateCustomboard(args.customgoals)
        if args.boardtype == 'balanced':
            generateBalancedBoard(args.boardsize, (float(args.difficulty.split('-')[0]), None, float(args.difficulty.split('-')[1])), args.pool)


    exit()



def getid(goal):
    for i in GOAL_INDEX:
        if GOAL_INDEX[i][0].lower() == goal.lower():
            print(f'>> {goal} has a goal ID of: {i}')
            return i
    print(f"Goal Lookup Error: {goal} is not a valid goal id")
    return "Goal not found."


def getrandomgoal():
    return choice(list(GOAL_INDEX))


def translate(goal_id):
    if str(goal_id).upper() in GOAL_INDEX:
        print(f'>> {goal_id} has a goal name of: {GOAL_INDEX[str(goal_id)][0]}')
        return GOAL_INDEX[str(goal_id)][0]
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
        while ((newgoal in boardBlueprint) or (GOAL_INDEX[newgoal][3] not in range(int(minDifficulty), int(maxDifficulty)+1)) 
                or (GOAL_INDEX[newgoal][3] != preferredDifficulty if preferredDifficulty != None else False)
                or checkExcludedGoals(newgoal, excluded)) or newgoal in boardBlueprint:
            newgoal = choice(goalPool)
            runs += 1
            if runs > 300:
                print(" > [Error] Failed to find compatible goal. Reverting to random non-duplicate.")
                break
        while newgoal in boardBlueprint:
            newgoal = choice(goalPool)

        boardBlueprint.append(newgoal)
        print(f' > Added {newgoal} ({GOAL_INDEX[newgoal][0]}) of difficulty {GOAL_INDEX[newgoal][3]}')

    generateBoard(boardBlueprint, f's{size}-d{minDifficulty}-{maxDifficulty}')
    return boardBlueprint


if __name__ == '__main__':
    main()
