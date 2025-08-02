from lockout import *
from create_listeners import createListeners
from create_triggers import createTriggers


def parseInput(userInput):
    splitBySpaces = userInput.split(' ')
    cmd = splitBySpaces[0]
    args = splitBySpaces[1:]
    flags = ''
    argsToRemove = []
    for i in range(len(args)):
        arg = args[i]
        if arg[0] == '-':
            flags += arg[1:]
            argsToRemove.append(i)
    for a in argsToRemove:
        args.pop(a)

    return cmd, flags, args


def generateCommand(flags, args):
    if len(args) < 3:
        print(f'Error - Invalid number of arguments for command "gen" (recieved {len(args)})')
        return True

    if args[0] == '--help':
        print('Generate a balanced board. Syntax: gen <type> <size> <difficulty-range>')

    boardType = args[0]
    boardSize = int(args[1])
    difficultyRange = args[2]
    minDifficulty = difficultyRange.split('-')[0]
    maxDifficulty = difficultyRange.split('-')[1]
    expansions = (['all'] if (len(args) <= 3) else args[3:])
    if boardType == 'b':
        generateBalancedBoard(boardSize, (minDifficulty, None, maxDifficulty), expansions)
        if 'q' in flags:
            print('Quit flag passed. Terminating after command finishes.')
            return False
    elif boardType == 'c':
        boardBlueprint = args[1:]
        generateCustomboard(boardBlueprint)
        if 'q' in flags:
            print('Quit flag passed. Terminating after command finishes.')
            return False
    else:
        print('Error - Board type not recognized. Please use either b (balanced) or c (custom)')

    return True


def inputLoop():

    userInput = input(">>> ")
    cmd, flags, args = parseInput(userInput)

    if cmd == 'exit':
        return False

    elif cmd == 'help':
        print('Help coming soon...')

    elif cmd == 'gen' or cmd == 'generate':
        return generateCommand(flags, args)

    elif cmd == 'createlisteners':
        createListeners()
        print('Created Listeners')

    elif cmd == 'createtriggers':
        createTriggers()
        print('Created Triggers')


    return True



if __name__ == "__main__":
    print('============================================')
    print('   Truffle Lockout Generator v2.0 (CLI)')
    print('============================================')
    while True:
        if not inputLoop():
            break
    print("Terminating...")
