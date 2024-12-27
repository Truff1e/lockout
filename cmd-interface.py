from lockout import *

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
   $getrandomgoal - Generates a random goal ID
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
            print(getrandomgoal())

        elif args[0] == 'getid':
            getid(args[1])

        elif args[0] == 'translate':
            translate(args[1])

        else:
            print('Unknown Command')


main()
