from generator import generateBoard
from index import goalDictionary, exclusiveSets, balancedIndex
from random import choice, choices

version = '1.7.4'

def customboard(goal_list: list):
    generateBoard(goal_list, f'random-s{len(goal_list)+1}', version)


def randomboard(size: int, overrides: list, excluded=None):
    if excluded is None:
        excluded = []
    goal_list = []

    for i in range(size):
        newgoal = choice(balancedIndex)
        runs = 0
        while newgoal in goal_list or check_exclusive_sets(newgoal, goal_list, overrides) or check_excluded_goals(newgoal, excluded):
            newgoal = choice(balancedIndex)
            runs += 1
            if runs > 300:
                print("Failed to find compatible goal, defaulting to random non-duplicate.")
                break
        while newgoal in goal_list:
            newgoal = choice(balancedIndex)
        print(f'Added {newgoal} ({goalDictionary[newgoal][0]}) of difficulty {goalDictionary[newgoal][2]}')
        goal_list.append(newgoal)

    generateBoard(goal_list, f'random-s{size}', version)


def balancedboard(size: int, difficulty, overrides: list, excluded=None):
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
        while (newgoal in goal_list) or (goalDictionary[newgoal][2] != goal_difficulty) or check_exclusive_sets(newgoal, goal_list, overrides) or check_excluded_goals(newgoal, excluded):
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


def check_exclusive_sets(goal: str, goal_list: list, overrides: list):
    if 'all' in overrides:
        return False
    else:
        for ex_set in exclusiveSets:
            if ex_set in overrides:
                continue
            if goal in exclusiveSets[ex_set]:
                for i in goal_list:
                    if i in exclusiveSets[ex_set]:
                        return True
        return False


def check_excluded_goals(goal, exclusion_sets):
    for exclusion_set in exclusion_sets:
        if goal in exclusion_set:
            return True
    return False


def check_cmd_args(args, min_args: int, board_size_check: bool):
    if len(args) == 1:
        print(">> ERROR: Invalid Arguments - See help page for more")
        return False
    elif not len(args) <= min_args:
        print(">> ERROR: Invalid Arguments - See help page for more")
        return False
    if board_size_check:
        if int(args[1]) > 9:
            print(">> ERROR: Invalid Board Size - Must be less than 10")
            return False
    return True
