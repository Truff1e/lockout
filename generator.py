import math
import shutil
from random import randint
from index import goalDictionary


def generateBoard(goals: list, user: str):
    version = '1.5.0-1.21.3'
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    board_size = len(goals)
    board_goals = []
    square = math.sqrt(board_size)

    for i in range(len(goals)):
        if goals[i] not in goalDictionary:
            return f"Error: Goal Lookup Error ({goals[i]} is not a valid goal)"

    if not square.is_integer():
        return f"Error: Board Size Error ({board_size})"
    else:
        file_path = f'./files/gen/lockout-{version}-{user}-{randint(10000, 99999)}'
        template_dir = './files/lockout_template'
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
            board_goals.append([goals[goal], coordinate])

        # write start function
        file = open(f'{file_path}/data/lockout/function/game/start.mcfunction', 'w')
        for col in range(int(math.sqrt(len(board_goals)))):
            file.write(f'advancement grant @a only lockout:board/{letters[col]}{int(math.sqrt(len(board_goals)))+1}\n')
        for goal in range(len(board_goals)):
            file.write(f'scoreboard players set #{board_goals[goal][0]} lk.enabled_goals 1\n')
        file.write('execute as @a run function lockout:game/countdown\n')
        file.write(f'scoreboard players set #boardSize lk.util {(len(board_goals)+1)//2}')
        file.close()

        # write resume function
        file = open(f'{file_path}/data/lockout/function/game/resume.mcfunction', 'w')
        for col in range(int(math.sqrt(len(board_goals)))):
            file.write(f'advancement grant @a only lockout:board/{letters[col]}{int(math.sqrt(len(board_goals)))+1}\n')
        for i in range(len(board_goals)):
            command = 'execute as @a[advancements={lockout:board/' + board_goals[i][1] + '=true}] run advancement grant @a only lockout:board/' + board_goals[i][1] + '\n'
            file.write(command)
        file.close()

        # write get-goals function
        file = open(f'{file_path}/data/lockout/function/game/getgoal.mcfunction', 'w')
        for i in range(len(board_goals)):
            number = board_goals[i][0].strip('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            file.write(f'execute if score @s lk.goal matches {ord((board_goals[i][0])[0])}{number} run advancement grant @a only lockout:board/{board_goals[i][1]}\n')
        file.close()

        # write advancement tree
        file = open(f'{file_path}/data/lockout/advancement/board/root.json', 'w')
        file.write('{\n"display": {\n"icon": {\n"id":"minecraft:ominous_trial_key","components": {"minecraft:custom_model_data": 1}\n},\n"title": "Lockout Board",\n"description": "Generated with the Truff1e Lockout Board Generator", \n"background": "minecraft:textures/block/stone.png",\n"frame": "task", \n"announce_to_chat": false, \n"hidden": false},\n"criteria": {"trigger": {"trigger": "minecraft:impossible"}}}')
        file.close()
        for i in range(len(board_goals)):
            letter, num = board_goals[i][1].strip('123456789'), int(board_goals[i][1].strip('abcdefghij'))
            if num == 1:
                parent = 'root'
            else:
                parent = f'{letter}{num-1}'
            goal = goalDictionary[board_goals[i][0]]

            file = open(f'{file_path}/data/lockout/advancement/board/{board_goals[i][1]}.json', 'w')
            file.write('{\n"display": {\n"icon": {\n' + goal[1] + '\n},\n"title": "' + goal[0] + '",\n"description": "", \n"frame": "task", \n"announce_to_chat": false, \n"hidden": false},\n')
            file.write(f'"parent": "lockout:board/{parent}",\n' + '"criteria": {"trigger": {"trigger": "minecraft:impossible"}}}')
        board_size = int(math.sqrt(len(board_goals)))
        for i in range(board_size):
            file = open(f'{file_path}/data/lockout/advancement/board/{letters[i]}{board_size+1}.json', 'w')
            file.write('{\n"display": {\n"icon": {\n "id": "minecraft:stone_button"\n},\n"title": "-",\n"description": "", \n"frame": "task", \n"announce_to_chat": false, \n"hidden": false},\n')
            file.write(f'"parent": "lockout:board/{letters[i]}{board_size}",\n' + '"criteria": {"trigger": {"trigger": "minecraft:impossible"}}}')
        return file_path
