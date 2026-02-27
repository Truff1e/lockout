import math
import shutil
import os
import datetime
import platform
import subprocess
from index import *


def open_directory(path):
    # Opens either Finder or File Explorer with the specified path
    if platform.system() == 'Windows':
        os.startfile(path)
    elif platform.system() == 'Darwin':
        subprocess.Popen(['open', path])
    else:
        print("Open Directory Failed - Unsupported platform")


def write_start_function(path, boardBlueprint):
    # Writes the function responsible for starting the game
    file = open(f'{path}/data/lockout/function/game/start.mcfunction', 'w')
    size = int(math.sqrt(len(boardBlueprint)))

    for col in range(size):
        # Grants players the cap advancements so that all parent advancements can be seen
        file.write(f'advancement grant @a only lockout:board/{chr(97+col)}{size+1}\n')

    for goalId, _, _ in boardBlueprint:
        # Enables the listeners for every goal on the board
        file.write(f'scoreboard players set #{goalId} lk.enabled_goals 1\n')

    # Starts the countdown and sets the board size
    file.write(f'execute unless score #blackout lk.util matches 1 run scoreboard players set #boardSize lk.util {(len(boardBlueprint)+1)//2}\n')
    file.write(f'execute if score #blackout lk.util matches 1 run scoreboard players set #boardSize lk.util {(len(boardBlueprint))}\n')
    file.write('execute as @a run function lockout:game/init\n')
    file.close()


def write_resume_function(path, boardBlueprint):
    # Writes the function responsible for "resuming" the game when a player leaves and rejoins
    file = open(f'{path}/data/lockout/function/game/resume.mcfunction', 'w')
    size = int(math.sqrt(len(boardBlueprint)))

    for col in range(size): 
        # Grants players the cap advancements so that all parent advancements can be seen
        file.write(f'advancement grant @a only lockout:board/{chr(97+col)}{size+1}\n')

    for _, coordinate, _ in boardBlueprint: # if goal is completed, give it to everyone
        file.write('execute as @a[advancements={lockout:board/' + coordinate + '=true}] run advancement grant @a only lockout:board/' + coordinate + '\n')

    file.write('execute as @s run function lockout:game/resume_moregoals')
    file.close()


def write_getgoals_function(path, boardBlueprint):
    # Writes the function to translate a scoreboard value into the correct advancement on the lockout board
    file = open(f'{path}/data/lockout/function/game/getgoal.mcfunction', 'w')
    for goalId, coordinate, _ in boardBlueprint:
        number = goalId[1:]
        file.write(f'execute if score @s lk.goal matches {ord(goalId[0])}{number} run advancement grant @a only lockout:board/{coordinate}\n')
    file.close()


def write_advancement_tree(path, boardBlueprint):
    # Writes the advancement files to display goals on the board
    for goalId, coordinate, goalInfo in boardBlueprint:
        if int(coordinate[1:]) == 1:
            parent = 'root'
        else:
            parent = coordinate[0] + str(int(coordinate[1:]) - 1)

        file = open(f'{path}/data/lockout/advancement/board/{coordinate}.json', 'w')
        if goalInfo[2]:
            file.write('{\n"display": {\n"icon": {\n"id": "minecraft:' + goalInfo[1] + '","components": {"minecraft:custom_model_data": {"strings": ["' + goalId + '"]}}\n},\n"title": "' + goalInfo[0] + '",\n"description": "", \n"frame": "task", \n"announce_to_chat": false, \n"hidden": false},\n')
        else:
            file.write('{\n"display": {\n"icon": {\n"id": "minecraft:' + goalInfo[1] + '"\n},\n"title": "' + goalInfo[0] + '",\n"description": "", \n"frame": "task", \n"announce_to_chat": false, \n"hidden": false},\n')
        file.write(f'"parent": "lockout:board/{parent}",\n' + '"criteria": {"trigger": {"trigger": "minecraft:impossible"}}}')
    boardSideLength = int(math.sqrt(len(boardBlueprint)))

    for i in range(boardSideLength):
        file = open(f'{path}/data/lockout/advancement/board/{chr(97+i)}{boardSideLength+1}.json', 'w')
        file.write('{\n"display": {\n"icon": {\n "id": "minecraft:stone_button"\n},\n"title": "-",\n"description": "",\n"show_toast": false,\n"frame": "task", \n"announce_to_chat": false, \n"hidden": false},\n')
        file.write(f'"parent": "lockout:board/{chr(97+i)}{boardSideLength}",\n' + '"criteria": {"trigger": {"trigger": "minecraft:impossible"}}}')


def write_info_file(path, boardBlueprint):
    file = open(f'{path}/board_info.txt', 'w')
    file.write(dumpGeneratorInfo())
    file.write('\nThis lockout board was generated using the Truff1e Lockout generator.\n')
    file.write('https://github.com/truff1e/lockout\n')
    file.write(f'Generated on: {datetime.datetime.now().strftime('%Y%m%d-%H%M')}\n') #TODO This does not account for time zones. Not a high priority issue
    file.write(f'Board Size: {len(boardBlueprint)}\n')
    file.write(f'Board: {boardBlueprint}\n')
    file.close()


def write_default_settings_file(path):
    file = open(f'{path}/data/lockout/function/settings/defaults.mcfunction', 'w')
    file.write(f'''
#if the game has already been initialized, don't reset the scores
execute if score #initialized lk.util matches 1 run return fail
#settings
scoreboard players set #start_time lk.util {LK_START_TIME}
scoreboard players set #max_time lk.util {LK_MAX_TIME}
scoreboard players set #show_progress lk.util {1 if LK_SHOW_PROGRESS else 0}
scoreboard players set #allow_pvp lk.util {1 if LK_ALLOW_PVP else 0}
scoreboard players set #allow_locator lk.util {1 if LK_ALLOW_TRACKER else 0}
scoreboard players set #allow_draw lk.util {1 if LK_ALLOW_DRAW else 0}
scoreboard players set #allow_resign lk.util {1 if LK_ALLOW_RESIGN else 0}
scoreboard players set #end_on_win lk.util {1 if LK_END_ON_WIN else 0}
scoreboard players set #friendly_fire lk.util {1 if LK_ALLOW_FRIENDLY_FIRE else 0}
scoreboard players set #show_timer lk.util {1 if LK_SHOW_TIMER else 0}
''')
    file.close()



def prepare_files(output_path, boardtype: str):
    datapack_version = f'v{VERSION}-{MCVERSION}'

    app_path = os.path.dirname(__file__)
    datapack_path = f'lockout-{datapack_version}-{boardtype}-{datetime.datetime.now().strftime('%Y%m%d-%H%M')}'
    filePath = os.path.join(output_path, datapack_path)

    template_dir = os.path.join(app_path, 'template')
    shutil.copytree(template_dir, filePath, dirs_exist_ok=True)
    return filePath


def clean_up(filePath):
    # make zip archive
    shutil.make_archive(filePath, 'zip', filePath)
    # delete folder
    shutil.rmtree(filePath)


def generateBoard(goals: list, boardtype: str):
    # Generates the lockout data pack based on a list of goal IDs
    board_size = len(goals)
    square = math.sqrt(board_size)

    for g in goals:
        if g not in GOAL_INDEX:
            print(f" > [Fatal Error] {g} is not a valid goal id")
            return False

    if not square.is_integer():
        print(f" > [Fatal Error] The amount of goals must be a square number (you had {board_size} goals)")
        return False

    else:

        boardBlueprint = []
        outputPath = os.path.join(os.path.expanduser('~'), OUTPUT_DIR)
        filePath = prepare_files(outputPath, boardtype)

        print(f"Creating a {int(square)}x{int(square)} board using:", ''.join(f'{str(goal)},' for goal in goals))  # logs a list of board goals

        # create goal/coordinate/info map (eg. ["K0023", "b2", ['Kill Zombie', 'iron_sword', True, 1]])
        for i in range(board_size):
            goalId = goals[i]
            letter = chr(97 + (i // int(square)))
            number = (i % int(square)) + 1
            coordinate = f'{letter}{number}'
            goalInfo = GOAL_INDEX[goalId]
            boardBlueprint.append((goalId, coordinate, goalInfo))

        # generate the necessary data pack files
        write_start_function(filePath, boardBlueprint)
        write_resume_function(filePath, boardBlueprint)
        write_getgoals_function(filePath, boardBlueprint)
        write_advancement_tree(filePath, boardBlueprint)
        write_info_file(filePath, boardBlueprint)
        write_default_settings_file(filePath)

        clean_up(filePath)
        open_directory(outputPath)
        print('Data Pack Created! Check', outputPath, 'for your zip file.')
        return True
