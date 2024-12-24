from generator import generateBoard
from index import goalDictionary, exclusiveSets, balancedIndex
from random import choice, choices

version = '1.7.1'

def customboard(goal_list: list):
    generateBoard(goal_list, f'random-s{len(goal_list)+1}', version)


def randomboard(size: int, overrides: list, excluded=None):
    if excluded is None:
        excluded = []
    goal_list = []

    for i in range(size):
        newgoal = choice(balancedIndex)
        print(newgoal)
        runs = 0
        while newgoal in goal_list or check_exclusive_sets(newgoal, goal_list, overrides) or check_excluded_goals(newgoal, excluded):
            newgoal = choice(balancedIndex)
            runs += 1
            if runs > 300:
                print("Failed to find compatible goal, defaulting to random non-duplicate.")
                break
        while newgoal in goal_list:
            newgoal = choice(balancedIndex)
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
            return
    print(">> Goal not found.")


def getrandomgoal(amount):
    for i in range(amount):
        print(choice(list(goalDictionary)))


def translate(goal_id):
    if str(goal_id).upper() in goalDictionary:
        print(f'>> {goal_id} has a goal name of: {goalDictionary[str(goal_id)][0]}')
        return
    else:
        print(">> Goal not found.")


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


def main():
    finished = False

    print(f'''
====================================================================
           >>> Lockout Generator v{version} is Ready <<<
         Enter a command to generate a board or type help
====================================================================  
    ''')

    while not finished:

        command = input(">> Lockout Generator: $")
        args = command.split(' ')

        if args[0] == 'help':
            print(f'''
>> LOCKOUT GENERATOR COMMAND MANUAL ===========================================================
   $help - Shows this page
   $exit - Closes the generator

>> BOARD GENERATOR COMMANDS ===================================================================
   $customboard <size> <goals> - Generates a board with a custom set of goals
   $balancedboard <size> <difficulty> %<overrides> - Generates a board with weighted difficulty
   $randomboard <size> %<overrides> - Generates a random board

>> GOAL LOOKUP COMMANDS =======================================================================
   $getrandomgoal <amount> - Generates a number of random goal IDs
   $getid <goal_name> - Gets the ID associated with a goal name
   $translate <goalID> - Translates a goal ID into its name
            ''')

        elif args[0] == 'exit':
            print('>> Exiting...')
            finished = True

        elif args[0] == 'customboard':
            print('>> Generating Custom Board')
            print('   Goals:', args[1].split(','))
            customboard(args[1].split(','))
            finished = True

        elif args[0] == 'balancedboard':
            if check_cmd_args(args, 4, True):
                print('>> Generating Balanced Board')
                print('   Size:', args[1])
                print('   Difficulty:', args[2].split(','))
                if '%' in command:
                    print('   Overrides:', args[3].strip('%').split(','))
                    balancedboard(int(args[1])**2, args[2].split(','), args[3].strip('%').split(','))
                else:
                    print('   Overrides: None Detected')
                    balancedboard(int(args[1])**2, args[2].split(','), [])
                finished = True

        elif args[0] == 'randomboard':
            if check_cmd_args(args, 2, True):
                print('>> Generating Random Board')
                print('   Size:', args[1])
                if '%' in command:
                    print('   Overrides:', args[2].strip('%').split(','))
                    randomboard((int(args[1])**2), args[2].strip('%').split(','))
                else:
                    print('   Overrides: None Detected')
                    randomboard(int(args[1])**2, [])
                finished = True

        elif args[0] == 'getrandomgoal':
            if len(args) < 2:
                print(getrandomgoal(1))
            else:
                getrandomgoal(int(args[1]))

        elif args[0] == 'getid':
            getid(args[1])

        elif args[0] == 'translate':
            translate(args[1])

        else:
            print('Unknown Command')


main()
