from generator import generateBoard
from index import goalIndex, parseGoalPool
from random import choice, choices
import os


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
    print(f'Generating Custom Board')
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
