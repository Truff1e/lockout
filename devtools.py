from index import GOAL_INDEX
import os
import argparse
import re
import json
from datetime import datetime, timedelta, time


def createGoalFunctions():
    path = './template/data/lockout/function/goals'
    # This is used to automatically generate all the functions that are called when a goal is achieved.
    print('[devtools] Creating goal functions...')
    try:
        os.mkdir(path)
    except FileExistsError:
        print('[devtools] Directory already exists. Proceeding...')
        pass

    for goal in GOAL_INDEX:
        file = open(f'{path}/{goal.lower()}.mcfunction', 'w')
        number = goal[1:]
        # Write most function for most goals
        if 'M' in goal:
            file.write("execute as @s run function lockout:goals/template/most {" + f'"goalid": "{goal}", "goalnum": "{ord(goal[0])}{number}", "goalname": "{GOAL_INDEX[goal][0]}"' + '}')
        # Write reversed function for Opponent goals
        elif 'N' in goal:
            file.write("execute as @s run function lockout:goals/template/opponent {" + f'"goalid": "{goal}", "goalnum": "{ord(goal[0])}{number}", "goalname": "{GOAL_INDEX[goal][0]}"' + '}')
        else:
            # Write goal triggers for all other goals
            file.write("execute as @s run function lockout:goals/template/default {" + f'"goalid": "{goal}", "goalnum": "{ord(goal[0])}{number}", "goalname": "{GOAL_INDEX[goal][0]}"' + '}')

        file.close()

    print('[devtools] Success!')




def createGrantFunctions():
    path = './template/data/lockout/function/grant'
    print('[devtools] Creating grant functions...')
    try:
        os.mkdir(path)
    except FileExistsError:
        print('[devtools] Directory already exists. Proceeding...')
        pass

    for id, goal in GOAL_INDEX.items():
        if id.startswith('N'): continue
        if id.startswith('M'): continue
        functionname = goal[0].lower().replace(' ', '_')
        goalnum = str(ord(id[0])) + id[1:]
        goalname = goal[0]
        file = open(f'{path}/{functionname}.mcfunction', 'w')
        file.write('execute as @s run function lockout:goals/template/default {"goalid": "' + id + '", "goalnum": "' + goalnum + '", "goalname": "' + goalname + '"}')
        file.close()
    print('[devtools] Success!')



def createRevokeFunctions():
    path = './template/data/lockout/function/revoke'
    print('[devtools] Creating revoke functions...')
    try:
        os.mkdir(path)
    except FileExistsError:
        print('[devtools] Directory already exists. Proceeding...')
        pass

    for id, goal in GOAL_INDEX.items():
        if id.startswith('N'): continue
        if id.startswith('M'): continue
        functionname = goal[0].lower().replace(' ', '_')
        goalnum = str(ord(id[0])) + id[1:]
        goalname = goal[0]
        file = open(f'{path}/{functionname}.mcfunction', 'w')
        file.write('execute as @a run function lockout:goals/template/revoke {"goalid": "' + id + '", "goalnum": "' + goalnum + '", "goalname": "' + goalname + '"}')
        file.close()
    
    print('[devtools] Success!')


def createGoalListeners():
    '''
    Attempts to auto-generate as many goal listeners as possible.
    '''
    try:
        os.mkdir('./listeners')
    except FileExistsError:
        print('Listeners directory already exists. Proceeding...')
        pass

    for goalId in GOAL_INDEX:

        template = '''{
    "criteria": {
      "<CRITERIA>": {
        "trigger": "minecraft:<TRIGGER>",
        "conditions": {
          "<CONDITION>": {
            <CONDITION_VALUE>
          }
        }
      }
    },
    "requirements": [
      [
        "<CRITERIA>"
      ]
    ],
    "rewards": {
      "function": "lockout:goals/<GOALID>"
    }
}'''

        item_template = '''{
    "criteria": {
      "<CRITERIA>": {
        "trigger": "minecraft:<TRIGGER>",
        "conditions": {
            "<CONDITION>": [
                {
                    <CONDITION_VALUE>
                }
            ]
        }
      }
    },
    "requirements": [
      [
        "<CRITERIA>"
      ]
    ],
    "rewards": {
      "function": "lockout:goals/<GOALID>"
    }
}'''
        goal = GOAL_INDEX[goalId]
        goalType = goalId[0]

        if goalType == 'I':
            criteria = 'getitem'
            item = goal[1]
            trigger = 'inventory_changed'
            condition = 'items'

            if '64' in goal[0]:
                condition_value = f'"items": "minecraft:{item}",\n"count": 64'
            else:
                condition_value = f'"items": "minecraft:{item}"'
        
            file = open(f'listeners/{goalId.lower()}.json', 'w')
            item_template = item_template.replace('<CRITERIA>', criteria)
            item_template = item_template.replace('<TRIGGER>', trigger)
            item_template = item_template.replace('<CONDITION>', condition)
            item_template = item_template.replace('<CONDITION_VALUE>', condition_value)
            item_template = item_template.replace('<GOALID>', goalId.lower())

            file.write(item_template)
            file.close()

        elif goalType == 'K':
            criteria = 'killentity'
            entity = goal[0][5:].lower().replace(' ', '_')
            trigger = 'player_killed_entity'
            condition = 'entity'
            condition_value = f'"type": "minecraft:{entity}"'
        
            file = open(f'listeners/{goalId.lower()}.json', 'w')
            template = template.replace('<CRITERIA>', criteria)
            template = template.replace('<TRIGGER>', trigger)
            template = template.replace('<CONDITION>', condition)
            template = template.replace('<CONDITION_VALUE>', condition_value)
            template = template.replace('<GOALID>', goalId.lower())

            file.write(template)
            file.close()

        elif goalType == 'D':
            criteria = 'dieto'
            entity = goal[0][7:].lower().replace(' ', '_')
            trigger = 'entity_killed_player'
            condition = 'entity'
            condition_value = f'"type": "minecraft:{entity}"'
        
            file = open(f'listeners/{goalId.lower()}.json', 'w')
            template = template.replace('<CRITERIA>', criteria)
            template = template.replace('<TRIGGER>', trigger)
            template = template.replace('<CONDITION>', condition)
            template = template.replace('<CONDITION_VALUE>', condition_value)
            template = template.replace('<GOALID>', goalId.lower())

            file.write(template)
            file.close()

        elif goalType == 'E':
            criteria = 'eat'
            food = goal[0][4:].lower().replace(' ', '_')
            trigger = 'consume_item'
            condition = 'item'
            condition_value = f'"items": "minecraft:{food}"'
        
            file = open(f'listeners/{goalId.lower()}.json', 'w')
            template = template.replace('<CRITERIA>', criteria)
            template = template.replace('<TRIGGER>', trigger)
            template = template.replace('<CONDITION>', condition)
            template = template.replace('<CONDITION_VALUE>', condition_value)
            template = template.replace('<GOALID>', goalId.lower())

            file.write(template)
            file.close()

        elif goalType == 'X' and goalId[1] == '1':
            criteria = 'effect'
            effect = goal[0][4:].lower().replace(' ', '_')
            trigger = 'effects_changed'
            condition = 'effects'
            condition_value = f'"minecraft:{effect}": ' + '{}'
        
            file = open(f'listeners/{goalId.lower()}.json', 'w')
            template = template.replace('<CRITERIA>', criteria)
            template = template.replace('<TRIGGER>', trigger)
            template = template.replace('<CONDITION>', condition)
            template = template.replace('<CONDITION_VALUE>', condition_value)
            template = template.replace('<GOALID>', goalId.lower())

            file.write(template)
            file.close()



def createGoalIdStrings(letter, length):
    '''
    Prints goal id numbers.
    '''
    for i in range(length):
        zeros = 4 - len(str(i+1)) 
        print(letter + ("0" * zeros) + str(i+1))


def createTextureTestFile():
    path = './template/data/lockout/function/settings'
    print('[devtools] Creating texture test file...')

    with open(f'{path}/test_textures.mcfunction', 'w') as file:
        for key, goal in GOAL_INDEX.items():
            file.write("give @s minecraft:" + goal[1] + "[custom_model_data={'strings':['" + key + "']}]\n")
        file.close()

    print('[devtools] Success!')


def filterGoalsForGoalPool():
    goals = []
    for id, goal in GOAL_INDEX.items():
        while True:
            is_to_add = input(f'Add goal {id} ({goal[0]}) to the pool? [y/n]')
            if is_to_add.lower() == 'y':
                goals.append(id)
                break
            elif is_to_add.lower() == 'n' or is_to_add == '':
                break
            else:
                print('Invalid response')

    for g in goals:
        print(f'"{g}",')




def parseLogFile(file):

    log = open(file, '+r')
    
    mode = 'scanning'
    goals = []
    start_time = datetime(year=1, month=1, day=1)
    end_type = None
    players = {}

    for line in log:

        if mode == 'scanning':
            start = re.match('\[(.*)\] \[.*Running function lockout.*', line)
            if start:
                start_time = datetime.strptime(start.groups()[0], '%H:%M:%S')
                print('Located Start Command at time', start_time)
                mode = 'game'
        elif mode == 'game':
            goal = re.match('\[(.*)\] \[.*\[(.*)\] completed \"(.*)\".*', line)
            failed_goal = re.match('\[(.*)\] \[.*\[(.*)\] failed \"(.*)\".*', line)

            if goal:
                time, player, goal = goal.groups()
                timecode = datetime.strptime(time, '%H:%M:%S')
                timestamp = timecode - start_time 
                goals.append({
                        "time": time,
                        "timestamp": f"{int(timestamp.total_seconds() // 60)}:{int(timestamp.total_seconds() % 60)}",
                        "player": player,
                        "goal": goal,
                        "failed": False,
                        "log_line": line,
                })

            if failed_goal:
                time, player, goal = failed_goal.groups()
                timecode = datetime.strptime(time, '%H:%M:%S')
                timestamp = timecode - start_time
                goals.append({
                        "time": time,
                        "timestamp": f"{int(timestamp.total_seconds() // 60)}:{int(timestamp.total_seconds() % 60)}",
                        "player": player,
                        "goal": goal,
                        "failed": True,
                        "log_line": line,
                })

            # end_type = re.match(".*Game Over - (.*)$", line)
            end = re.match(".*wins!.*", line)

            if end:
                mode = 'end'
                print(f'Game Over')

        elif mode == 'end':
            pass
            # max_time = 
            # duration = 
            # team1score = 
            # team2score = 
            # goals, failed, deaths, kills = 


    game_data = {
        "start_time": start_time.strftime('%H:%M:%S'),
        "goals": goals,
        # "end_type": end_type,
        # "players": players,
    }

    print(json.dumps(game_data, indent=4))
    return game_data


def createCraftFiles():
    item_ids = []
    path = './template/data/lockout/advancement/unique_crafts'
    print('[devtools] Creating recipe advancements...')

    for recipe in open('./recipies.txt', 'r').readlines():
        item_ids.append((recipe.strip(' '))[:-6])

    try:
        os.mkdir(path)
    except FileExistsError:
        print('[devtools] Directory already exists. Proceeding...')
        pass

    for item in item_ids:
        with open(f'{path}/{item}.json', 'w') as file:
            advancement = str('{"criteria": {"craft": {"trigger": "minecraft:recipe_crafted","conditions": {"recipe_id": "' + f'minecraft:{item}"' + '}}},"requirements": [["craft"]],"rewards": {"function": "lockout:goals/count_crafts"}}')
            file.write(advancement)
            file.close()

    print('[devtools] Success!')


def main():
    parser = argparse.ArgumentParser(description='Run tools for generating data pack files')

    parser.add_argument('function')

    args = parser.parse_args()

    if args.function == 'bootstrap':
        createGoalFunctions()
        createCraftFiles()
        createTextureTestFile()
        createRevokeFunctions()
        createGrantFunctions()
    else:
        print('[devtools] Unknown argument. Import devtools to use all its functions.')


if __name__ == '__main__':
    main()
