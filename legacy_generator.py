from generator import generateBoard
from index import goalDictionary, exclusiveSets
from random import choice, choices

# DEPRECATED - Supported until 1.6.0

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
            generateBoard(goals_list, f'custom')
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