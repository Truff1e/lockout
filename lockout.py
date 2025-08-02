from generator import generateBoard
from index import createNewBalancedGoalIndex, getFullGoalIndex
from random import choice, choices
import os

goalDictionary = getFullGoalIndex()

def getid(goal):
    for i in goalDictionary:
        if goalDictionary[i][0].lower() == goal.lower():
            print(f'>> {goal} has a goal ID of: {i}')
            return i
    print(f"Goal Lookup Error: {goal} is not a valid goal id")
    return "Goal not found."


def getrandomgoal():
    return choice(list(goalDictionary))


def translate(goal_id):
    if str(goal_id).upper() in goalDictionary:
        print(f'>> {goal_id} has a goal name of: {goalDictionary[str(goal_id)][0]}')
        return goalDictionary[str(goal_id)][0]
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


def parse_options():
    optionsfile = open(os.path.join(os.path.dirname(__file__), 'options.txt'), 'r')
    optionslist = {}
    for line in optionsfile:
        optionslist[line[:line.find('=')]] = line[line.find('=')+1:]
    return optionslist


version = parse_options()['version'][:-1]

def generateCustomboard(boardBlueprint: list):
    print(f'Generating Custom Board')
    generateBoard(boardBlueprint, f'custom-s{len(boardBlueprint)}', version)
    return boardBlueprint


def generateBalancedBoard(size: int, difficultySet: tuple, expansions, excluded=None):
    if excluded is None:
        excluded = []

    minDifficulty, difficultyWeights, maxDifficulty = difficultySet
    goalIndex = createNewBalancedGoalIndex(expansions, True)

    print(f'Generating Balanced Board of size {size}')

    boardBlueprint = [] 
    for i in range(size):
        if difficultyWeights != None:
            preferredDifficulty = choices(range(minDifficulty, maxDifficulty+1), weights=difficultyWeights, k=1)[0]
        else:
            preferredDifficulty = None

        newgoal = choice(list(goalIndex))
        runs = 0
        while ((newgoal in boardBlueprint) or (goalDictionary[newgoal][3] not in range(int(minDifficulty), int(maxDifficulty)+1)) 
                or (goalDictionary[newgoal][3] != preferredDifficulty if preferredDifficulty != None else False)
                or checkExcludedGoals(newgoal, excluded)) or newgoal in boardBlueprint:
            newgoal = choice(list(goalIndex))
            runs += 1
            if runs > 300:
                print("Failed to find compatible goal, defaulting to random non-duplicate.")
                break
        while newgoal in boardBlueprint:
            newgoal = choice(list(goalIndex))

        boardBlueprint.append(newgoal)
        print(f'Added {newgoal} ({goalDictionary[newgoal][0]}) of difficulty {goalDictionary[newgoal][3]}')

    generateBoard(boardBlueprint, f's{size}-d{minDifficulty}-{maxDifficulty}', version)
    return boardBlueprint
