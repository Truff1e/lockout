from generator import generateBoard
from index import goalDictionary, exclusiveSets
from random import choice, choices
import math
import shutil

version = '1.5.0'

def customboard(size: int, goal_list: list):

    print(f'Generating board with: {goal_list}')
    filepath = generateBoard(goal_list, f'random-s{size}')
    if filepath[0] == '.':
        shutil.make_archive(filepath, 'zip', filepath)
        print('Zip File Created!')
        print('Check ./files/gen for your data pack')
    else:
        print(f"An error occurred: {filepath}")

def randomboard(size: int, overrides: list):
    goal_list = []

    for i in range(size):
        newgoal = choice(list(goalDictionary))
        print(newgoal)
        runs = 0
        while newgoal in goal_list or check_exclusive_sets(newgoal, goal_list, overrides):
            newgoal = choice(list(goalDictionary))
            runs += 1
            if runs > 300:
                print("Failed to find compatible goal, defaulting to random non-duplicate.")
                break
        while newgoal in goal_list:
            newgoal = choice(list(goalDictionary))
        goal_list.append(newgoal)

    print(f'Generating board with: {goal_list}')
    filepath = generateBoard(goal_list, f'random-s{size}')
    if filepath[0] == '.':
        shutil.make_archive(filepath, 'zip', filepath)
        print('Zip File Created!')
        print('Check ./files/gen for your data pack')
    else:
        print(f"An error occurred: {filepath}")


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


def balancedboard(size: int, difficulty, overrides: list):

    # difficulty = input('Difficulty: ').split(',')
    if len(difficulty) > 1:
        weights = []
        for i in range(len(difficulty)):
            weights.append(int(difficulty[i]))
        difficulty = 'custom'
    else:
        difficulty = float(difficulty[0])
        while not 1 <= difficulty <= 7:
            print('Error: Difficulty out of range. (Must be between 1 and 6)')
            difficulty = int(input('Difficulty: '))
        weights = [(8 * -2**((difficulty-2.5)/6)) + 15, (8 * -2**((difficulty-2.5)/14)) + 15, (8 * 2**((difficulty-2.5)/5)) - 7.5, (8 * 2**((difficulty-2.5)/6)) - 9]

    # overrides = input('Override Exclusive Sets: ').split(' ')

    goal_list = []
    for w in range(len(weights)):
        if weights[w] < 0:
            weights[w] = 0
    for i in range(size):
        goal_difficulty = choices([1, 2, 3, 4], weights=weights, k=1)[0]
        newgoal = choice(list(goalDictionary))
        runs = 0
        while (newgoal in goal_list) or (goalDictionary[newgoal][2] != goal_difficulty) or check_exclusive_sets(newgoal, goal_list, overrides):
            newgoal = choice(list(goalDictionary))
            runs += 1
            if runs > 300:
                print("Failed to find compatible goal, defaulting to random non-duplicate.")
                break
        while newgoal in goal_list:
            newgoal = choice(list(goalDictionary))

        goal_list.append(newgoal)
        print(f'Added {newgoal} ({goalDictionary[newgoal][0]}) of difficulty {goalDictionary[newgoal][2]}')

    print(f'Generating board with: {goal_list}')
    filepath = generateBoard(goal_list, f's{size}-d{difficulty}')
    if filepath[0] == '.':
        shutil.make_archive(filepath, 'zip', filepath)
        print('Zip File Created!')
        print(filepath)
        print('Check ./files/gen for your data pack')
    else:
        print(f"An error occured: {filepath}")


def getid(goal):
    for i in goalDictionary:
        if goalDictionary[i][0].lower() == goal.lower():
            print(f'{goal} has a goal ID of: {i}')
            return
    print("Goal not found.")


def getrandomgoal(amount):
    for i in range(amount):
        print(choice(list(goalDictionary)))


def translate(goal_id):
    if str(goal_id).upper() in goalDictionary:
        print(f'{goal_id} has a goal name of: {goalDictionary[str(goal_id)][0]}')
        return
    else:
        print("Goal not found.")


def boardcreator():
    finished = False
    goals_list = []

    print(
        "Add a goal by inputting its ID or name. You can also generate a completely random board, or a more balanced "
        "board using 'randomboard' or 'balancedboard'. If you input goals manually, type 'generate' when you are "
        "ready to generate the board. Type 'del' to delete the last input or add an index number to delete a certain "
        "index. Type 'exit' to quit. Type 'commands' for more commands.")

    while not finished:
        inp = input(f'Next Goal: [{len(goals_list)} goals added] ')
        if inp == 'generate':
            file_path = generateBoard(goals_list, f'custom')
            if file_path[0] == '.':
                shutil.make_archive(file_path, 'zip', file_path)
                print('Zip File Created!')
                print('Check ./files/gen for your data pack')
            else:
                print(f"An error occured: {file_path}")
            print("Exiting...")
            finished = True

        elif 'del' in inp:
            try:
                num = int(inp.strip('del'))
                try:
                    goals_list.pop(num)
                except IndexError:
                    print('Error: Index out of range.')
            except ValueError:
                goals_list.pop()

        elif inp == 'print':
            print(goals_list)

        elif inp == 'load':
            goals_list = input("List of goals: ").split(' ')

        elif inp == 'randomgoal':
            getrandomgoal(int(input("Amount: ")))

        elif inp == 'randomboard':
            randomboard()
            print("Exiting...")
            finished = True

        elif inp == 'balancedboard':
            balancedboard()
            print("Exiting...")
            finished = True

        elif 'translate' in inp:
            translate(input('Goal ID to translate: '))

        elif 'getid' in inp:
            getid(input('Goal name to translate: '))

        elif 'dumpgoals' in inp:
            for i in goalDictionary:
                print(f'{i}: "{goalDictionary[i][0]}"')

        elif inp == 'printnames':
            for i in goals_list:
                print(i, ": ", goalDictionary[i][0])

        elif inp == 'exit':
            print("Exited.")
            finished = True

        elif inp == 'commands':
            print(
                'LOCKOUT COMMANDS '
                '========================================================================================\n'
                'del<index> - Delete an entry from your goal list (defaults to deleting last entry if no index '
                'specified\nprint - Print your goal list\nprintnames - Print your goal list with goal '
                'names\ntranslate - Translate a goal ID to its goal name\ngetid - Translate a goal name to its goal '
                'ID\ndumpgoals - Print the contents of the goal index\ngenerate - Generate a data pack based on your '
                'current list\nrandomboard - Generate a random board of a specified size (ignores manual '
                'list)\nbalancedboard - Generate a balanced board of a specified size and difficulty (ignores manual '
                'list)\nexit - Stops the program\n'
                '=====================================================================================================')

        else:
            name_found = False
            for i in goalDictionary:
                if goalDictionary[i][0].lower() == inp.lower():
                    goals_list.append(i)
                    name_found = True
            if inp in goalDictionary:
                goals_list.append(inp)
            elif name_found:
                pass
            else:
                print('Error: Invalid Goal')

def main():
    finished = False

    print("====================================================================")
    print(f"Lockout Generator v{version} is Ready")
    print("Enter a command to generate a board or type 'help' for the help page")
    print("====================================================================")

    while not finished:

        command = input(">> Lockout Generator: $")
        args = command.split(' ')

        if args[0] == 'help':
            print(f'''
============================================================================================
Lockout Generator v{version} Command Manual
$help - Shows this page
$exit - Closes the generator
============================================================================================
BOARD GENERATOR COMMANDS
$customboard <size> <goals> - Generates a board with a custom set of goals
$boardcreator - Opens the board creator assistant
$balancedboard <size> <difficulty> %<overrides> - Generates a balanced board with weighted difficulty
$randomboard <size> %<overrides> - Generates a random board with optional exclusive set overrides
============================================================================================
GOAL LOOKUP COMMANDS
$getrandomgoal <amount> - Generates a number of random goal IDs
$getid <goal_name> - Gets the ID associated with a goal name
$translate <goalID> - Translates a goal ID into its name
============================================================================================
            ''')

        elif args[0] == 'exit':
            print('Exiting...')
            finished = True

        elif args[0] == 'customboard':
            if not len(args) > 1:
                print("Error: Invalid Arguments")
            elif int(args[1]) > 9:
                print("Error: Invalid Board Size Argument")
            else:
                print('Generating Custom Board')
                print('Size:', args[1])
                print('Goals:', args[2].split(','))
                customboard((int(args[1])**2), args[2].split(','))

        elif args[0] == 'boardcreator':
            print('Opening Board Creator...')
            boardcreator()

        elif args[0] == 'balancedboard':
            if not len(args) > 2:
                print("Error: Invalid Arguments")
            elif int(args[1]) > 9:
                print("Error: Invalid Board Size Argument")
            elif '%' in command:
                print('Generating Balanced Board')
                print('Size:', args[1])
                print('Difficulty:', list(args[2]))
                print('Overrides:', args[3].strip('%').split(','))
                balancedboard(int(args[1])**2, args[2].split(','), args[3].strip('%').split(','))
            else:
                print('Generating Balanced Board')
                print('Size:', args[1])
                print('Difficulty:', list(args[2]))
                print('Overrides: None Detected')
                balancedboard(int(args[1])**2, args[2].split(','), [])

        elif args[0] == 'randomboard':
            if not len(args) > 1:
                print("Error: Invalid Arguments")
            elif int(args[1]) > 9:
                print("Error: Invalid Board Size Argument")
            elif '%' in command:
                print('Generating Random Board')
                print('Size:', args[1])
                print('Overrides:', args[2].strip('%').split(','))
                randomboard((int(args[1])**2), args[2].strip('%').split(','))
            else:
                print('Generating Random Board')
                print('Size:', args[1])
                print('Overrides: None Detected')
                randomboard(int(args[1])**2, [])

        elif args[0] == 'getrandomgoal':
            getrandomgoal(int(args[1]))

        elif args[0] == 'getid':
            getid(args[1])

        elif args[0] == 'translate':
            translate(args[1])

        else:
            print('Unknown Command')


main()
