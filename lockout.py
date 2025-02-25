from generator import generateBoard
from index import goalDictionary, balancedIndex
from random import choice, choices
import os

def parse_options():
    optionsfile = open(os.path.join(os.path.dirname(__file__), 'options.txt'), 'r')
    optionslist = {}
    for line in optionsfile:
        optionslist[line[:line.find('=')]] = line[line.find('=')+1:]
    return optionslist


version = parse_options()['version'][:-1]

def customboard(goal_list: list):
    generateBoard(goal_list, f'custom-s{len(goal_list)}', version)
    return goal_list


def balancedboard(size: int, difficulty, excluded=None):
    if excluded is None:
        excluded = []

    if len(difficulty) > 1:
        for w in range(len(difficulty)):
            difficulty[w] = float(difficulty[w])
        weights = difficulty
        difficulty = 'custom'
    else:
        difficulty = float(difficulty[0])
        while not 1 <= difficulty <= 8:
            print('Error: Difficulty out of range. (Must be between 1 and 8)')
            difficulty = int(input('Difficulty: '))
        weights = [(-0.5*difficulty) + 10, (-0.25*difficulty) + 8, (8 * 2**((difficulty-2.5)/8)) - 7.5, (8 * 2**((difficulty-2.5)/6)) - 9]

    goal_list = []
    for w in range(len(weights)):
        if weights[w] < 0:
            weights[w] = 0
    for i in range(size):
        goal_difficulty = choices([1, 2, 3, 4], weights=weights, k=1)[0]
        newgoal = choice(balancedIndex)
        runs = 0
        while ((newgoal in goal_list)
               or (goalDictionary[newgoal][2] != goal_difficulty)
               or check_excluded_goals(newgoal, excluded)):
            newgoal = choice(balancedIndex)
            runs += 1
            if runs > 300:
                print("Failed to find compatible goal, defaulting to random non-duplicate.")
                break
        while newgoal in goal_list:
            newgoal = choice(balancedIndex)

        goal_list.append(newgoal)
        print(f'Added {newgoal} ({goalDictionary[newgoal][0]}) of difficulty {goalDictionary[newgoal][2]}')

    generateBoard(goal_list, f's{size}-d{difficulty}', version)
    return goal_list


def getid(goal):
    for i in goalDictionary:
        if goalDictionary[i][0].lower() == goal.lower():
            print(f'>> {goal} has a goal ID of: {i}')
            return i
    print(">> Goal not found.")
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


def check_excluded_goals(newgoal, excluded):
    for goal in excluded:
        if newgoal == goal:
            return True
            # Goal is excluded
    return False
    # Goal is not excluded
