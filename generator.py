import math
import shutil
from random import randint
from index import goalDictionary

def write_start_function(path, goals, letters):
    file = open(f'{path}/data/lockout/function/game/start.mcfunction', 'w')
    for col in range(int(math.sqrt(len(goals)))):
        file.write(f'advancement grant @a only lockout:board/{letters[col]}{int(math.sqrt(len(goals)))+1}\n')
    for goal in range(len(goals)):
        file.write(f'scoreboard players set #{goals[goal][0]} lk.enabled_goals 1\n')
    file.write('execute unless score #blackout lk.util matches 1 as @a run function lockout:game/countdown\n')
    file.write(f'execute unless score #blackout lk.util matches 1 scoreboard players set #boardSize lk.util {(len(goals)+1)//2}')
    file.write('execute if score #blackout lk.util matches 1 as @a run function lockout:game/blackout_countdown\n')
    file.write(f'execute if score #blackout lk.util matches 1 scoreboard players set #boardSize lk.util {(len(goals))}')
    file.close()


def write_resume_function(path, goals, letters):
    file = open(f'{path}/data/lockout/function/game/resume.mcfunction', 'w')
    for col in range(int(math.sqrt(len(goals)))):
        file.write(f'advancement grant @a only lockout:board/{letters[col]}{int(math.sqrt(len(goals)))+1}\n')
    for i in range(len(goals)):
        command = 'execute as @a[advancements={lockout:board/' + goals[i][1] + '=true}] run advancement grant @a only lockout:board/' + goals[i][1] + '\n'
        file.write(command)
    file.close()


def write_getgoals_function(path, goals):
    file = open(f'{path}/data/lockout/function/game/getgoal.mcfunction', 'w')
    for i in range(len(goals)):
        number = goals[i][0].strip('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        file.write(f'execute if score @s lk.goal matches {ord((goals[i][0])[0])}{number} run advancement grant @a only lockout:board/{goals[i][1]}\n')
    file.close()


def write_advancement_tree(path, goals, letters):
    file = open(f'{path}/data/lockout/advancement/board/root.json', 'w')
    file.write('{\n"display": {\n"icon": {\n"id":"minecraft:ominous_trial_key","components": {"minecraft:custom_model_data": 1}\n},\n"title": "Lockout Board",\n"description": "Generated with the Truff1e Lockout Board Generator", \n"background": "minecraft:textures/block/stone.png",\n"frame": "task", \n"announce_to_chat": false, \n"hidden": false},\n"criteria": {"trigger": {"trigger": "minecraft:impossible"}}}')
    file.close()
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
    datapack_version = f'{version}-1.21.3'
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    board_size = len(goals)
    goal_list = []
    square = math.sqrt(board_size)

    for i in range(len(goals)):
        if goals[i] not in goalDictionary:
            print(f"Error: Goal Lookup Error ({goals[i]} is not a valid goal)")
            return False

    if not square.is_integer():
        print(f"Error: Board Size Error ({board_size})")
        return False

    else:
        # prepare template and file path
        file_path = f'datapacks/lockout-{datapack_version}-{user}-{randint(10000, 99999)}'
        template_dir = 'template'
        shutil.copytree(template_dir, file_path, dirs_exist_ok=True)

        goal_string = ''
        for goal in goals:
            goal_string += f'{str(goal)},'
        print(f"Creating a {int(square)}x{int(square)} board using:", goal_string)

        # create goal/coordinate map
        for goal in range(board_size):
            letter = letters[goal // int(square)]
            number = (goal % int(square)) + 1
            coordinate = f'{letter}{number}'
            goal_list.append([goals[goal], coordinate])

        write_start_function(file_path, goal_list, letters)

        write_resume_function(file_path, goal_list, letters)

        write_getgoals_function(file_path, goal_list)

        write_advancement_tree(file_path, goal_list, letters)

        # make archive
        shutil.make_archive(file_path, 'zip', file_path)
        shutil.rmtree(file_path)
        print('Data Pack Created!')
        print('Check the datapacks folder for your zip file.')

        return True
