import math
import shutil
import os
from random import randint
from index import goalDictionary
import platform
import subprocess

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

def open_directory(path):
    # Opens either Finder or File Explorer with the specified path
    if platform.system() == 'Windows':
        os.startfile(path)
    elif platform.system() == 'Darwin':
        subprocess.Popen(['open', path])
    else:
        return False

def parse_options():
    # Reads data stored in options.txt and translates it to a settings list
    optionsfile = open(os.path.join(os.path.dirname(__file__), 'options.txt'), 'r')
    optionslist = {}
    for line in optionsfile:
        optionslist[line[:line.find('=')]] = line[line.find('=')+1:]
    return optionslist

def write_start_function(path, goals):
    # Writes the mcfunction responsible for starting the game
    file = open(f'{path}/data/lockout/function/game/start.mcfunction', 'w')
    for col in range(int(math.sqrt(len(goals)))):
        # Grants players the cap advancements so that all parent advancements can be seen
        file.write(f'advancement grant @a only lockout:board/{letters[col]}{int(math.sqrt(len(goals)))+1}\n')
    for goal in range(len(goals)):
        # Enables the listeners for every goal on the board
        file.write(f'scoreboard players set #{goals[goal][0]} lk.enabled_goals 1\n')
    # Starts the countdown and sets the board size
    file.write('execute unless score #blackout lk.util matches 1 as @a run function lockout:game/countdown\n')
    file.write(f'execute unless score #blackout lk.util matches 1 run scoreboard players set #boardSize lk.util {(len(goals)+1)//2}\n')
    file.write('execute if score #blackout lk.util matches 1 as @a run function lockout:game/blackout_countdown\n')
    file.write(f'execute if score #blackout lk.util matches 1 run scoreboard players set #boardSize lk.util {(len(goals))}')
    file.close()


def write_resume_function(path, goals):
    # Writes the mcfunction responsible for "resuming" the game when a player leaves and rejoins
    file = open(f'{path}/data/lockout/function/game/resume.mcfunction', 'w')
    for col in range(int(math.sqrt(len(goals)))):
        file.write(f'advancement grant @a only lockout:board/{letters[col]}{int(math.sqrt(len(goals)))+1}\n')
    for i in range(len(goals)):
        command = 'execute as @a[advancements={lockout:board/' + goals[i][1] + '=true}] run advancement grant @a only lockout:board/' + goals[i][1] + '\n'
        file.write(command)
    file.write('execute as @s run function lockout:game/resume_moregoals')
    file.close()


def write_getgoals_function(path, goals):
    # Writes the function to translate a scoreboard value into the correct advancement on the lockout board
    file = open(f'{path}/data/lockout/function/game/getgoal.mcfunction', 'w')
    for i in range(len(goals)):
        number = goals[i][0].strip('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        file.write(f'execute if score @s lk.goal matches {ord((goals[i][0])[0])}{number} run advancement grant @a only lockout:board/{goals[i][1]}\n')
    file.close()


def write_advancement_tree(path, goals):
    # Writes the advancement files to display goals on the board
    for i in range(len(goals)):
        letter, num = goals[i][1].strip('123456789'), int(goals[i][1].strip('abcdefghij'))
        if num == 1:
            parent = 'root'
        else:
            parent = f'{letter}{num-1}'
        goal = goalDictionary[goals[i][0]]

        file = open(f'{path}/data/lockout/advancement/board/{goals[i][1]}.json', 'w')
        file.write('{\n"display": {\n"icon": {\n' + goal[1] + '\n},\n"title": "' + goal[0] + '",\n"description": "", \n"frame": "task", \n"announce_to_chat": false, \n"hidden": false},\n')
        file.write(f'"parent": "lockout:board/{parent}",\n' + '"criteria": {"trigger": {"trigger": "minecraft:impossible"}}}')
    board_size = int(math.sqrt(len(goals)))
    for i in range(board_size):
        file = open(f'{path}/data/lockout/advancement/board/{letters[i]}{board_size+1}.json', 'w')
        file.write('{\n"display": {\n"icon": {\n "id": "minecraft:stone_button"\n},\n"title": "-",\n"description": "",\n"show_toast": false,\n"frame": "task", \n"announce_to_chat": false, \n"hidden": false},\n')
        file.write(f'"parent": "lockout:board/{letters[i]}{board_size}",\n' + '"criteria": {"trigger": {"trigger": "minecraft:impossible"}}}')


def generateBoard(goals: list, user: str, version):
    # Generates the lockout data pack based on a list of goal IDs
    datapack_version = f'{version}-1.21.4'
    board_size = len(goals)
    goal_list = []
    square = math.sqrt(board_size)

    for g in goals:
        if g not in goalDictionary:
            print(f"Error: Goal Lookup Error ({g} is not a valid goal)")
            return False

    if not square.is_integer():
        print(f"Error: Board Size Error ({board_size})")
        return False

    else:
        # prepare template and file path
        app_path = os.path.dirname(__file__)
        output_path = os.path.join(os.path.expanduser('~'), parse_options()['output_path'])
        datapack_path = f'lockout-{datapack_version}-{user}-{randint(10000, 99999)}'
        file_path = os.path.join(output_path, datapack_path)
        template_dir = os.path.join(app_path, 'template')
        shutil.copytree(template_dir, file_path, dirs_exist_ok=True)

        goal_string = ''
        for goal in goals:
            goal_string += f'{str(goal)},'
        print(f"Creating a {int(square)}x{int(square)} board using:", goal_string)

        # create goal/coordinate map (eg. [K0023, b2])
        for goal in range(board_size):
            letter = letters[goal // int(square)]
            number = (goal % int(square)) + 1
            coordinate = f'{letter}{number}'
            goal_list.append([goals[goal], coordinate])

        write_start_function(file_path, goal_list)

        write_resume_function(file_path, goal_list)

        write_getgoals_function(file_path, goal_list)

        write_advancement_tree(file_path, goal_list)

        # make zip archive
        shutil.make_archive(file_path, 'zip', file_path)
        # delete folder
        shutil.rmtree(file_path)
        open_directory(output_path)
        print('Data Pack Created! Check', parse_options()['output_path'], 'for your zip file.')

        return True
