from lockout import *
from devtools import *


# global variables
gameVersion = '1.21.8'
disabledGoals = []


def safelyGetArgAtIndex(args, targetIndex, targetType):
    try:
        value = args[targetIndex]
        if type(value) == targetType:
            return value
        else:
            print(f'TypeError - Invalid type for argument {targetIndex} (recieved {type(args[targetIndex])})')
            return None
    except IndexError:
        print(f'IndexError - Invalid number of arguments (recieved {len(args)})')
        return None


def parseInput(userInput):
    splitBySpaces = userInput.split(' ')
    cmd = splitBySpaces[0]
    args = splitBySpaces[1:]
    flags = ''
    kwflags = {}
    argsToRemove = []
    for i in range(len(args)):
        arg = args[i]
        if arg[0:2] == '--':
            if len(args) > i+1:
                kwflags[arg[2:]] = args[i+1]
                argsToRemove.append(i+1)
            else:
                kwflags[arg[2:]] = None
            argsToRemove.append(i)
        elif safelyGetArgAtIndex(arg, 0, str) == '-':
            flags += arg[1:]
            argsToRemove.append(i)
    for a in argsToRemove:
        args.pop(a)

    return cmd, args, flags, kwflags



def createCommand(args, flags, kwflags):
    if 'help' in kwflags:
        print('Automatically generate data pack files for the template data pack. (Used in development, not a production feature)')
        return

    arg = safelyGetArgAtIndex(args, 0, str)
    if arg == None: return


    if arg == 'triggers':
        createTriggers()
        print('Created Triggers')
    elif arg == 'listeners':
        createListeners()
        print('Created Listeners')
    elif arg == 'craftfiles':
        createCraftFiles()
        print('Created Craft Files')
    else:
        print('Error - Unknown argument')



def generateCommand(args, flags, kwflags):

    if 'help' in kwflags:
        print('Generate a balanced board. Syntax: gen <type> <size> <difficulty-range>')
        return

    boardType = safelyGetArgAtIndex(args, 0, str)
    if boardType == None: return

    if boardType == 'b':
        boardSize = safelyGetArgAtIndex(args, 1, str)
        if boardSize == None: return
        boardSize = int(boardSize) 
        difficultyRange = args[2]
        minDifficulty = difficultyRange.split('-')[0]
        maxDifficulty = difficultyRange.split('-')[1]
        expansions = (['all'] if (len(args) <= 3) else args[3:])
        if len(args) < 3:
            print(f'Error - Invalid number of arguments for command "gen" with boardType "b" (recieved {len(args)})')
        generateBalancedBoard(boardSize, (minDifficulty, None, maxDifficulty), expansions)

    elif boardType == 'c':
        if len(args) < 2:
            print(f'Error - Invalid number of arguments for command "gen" with boardType "c" (recieved {len(args)})')
        boardBlueprint = args[1:]
        generateCustomboard(boardBlueprint)

    else:
        print('Error - Board type not recognized. Please use either b (balanced) or c (custom)')


def inputLoop():

    userInput = input(">>> ")
    cmd, args, flags, kwflags = parseInput(userInput)

    if cmd == 'exit':
        return False

    elif cmd == 'help' or cmd == 'q':
        print('Help coming soon...')

    elif cmd == 'gen' or cmd == 'generate':
        generateCommand(args, flags, kwflags)

    elif cmd == 'create':
        createCommand(args, flags, kwflags)

    if 'q' in flags:
        print('Quit flag passed. Terminating after command finishes.')
        return False

    return True



if __name__ == "__main__":
    print('======================================================')
    print('    ***  Truffle Lockout Generator v2.0 CLI  ***')
    print('               for MC 1.21.4-1.21.8')
    print('======================================================')

    while True:
        if not inputLoop():
            break
    print("Terminating...")
