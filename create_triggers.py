from index import goalDictionary, unique_advancements, have_more_goals
import os

# This is used to automatically generate all the functions that are called when a goal is achieved.

try:
    os.mkdir('./triggers')
except FileExistsError:
    print('Triggers directory already exists. Proceeding...')
    pass

for goal in goalDictionary:
    file = open(f'./triggers/{goal.lower()}.mcfunction', 'w')
    number = goal.strip('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    # Ensure goals that use achievement triggers are counted for unique advancements
    if 'A' in goal and goal not in unique_advancements:
        file.write('execute as @s run function lockout:goals/count/advancements\n')

    # Write most function for Most goals
    if goal in have_more_goals:
        file.write("execute as @s run function lockout:goals/skeleton/most {" + f'"goalid": "{goal}", "goalnum": "{ord(goal[0])}{number}", "goalname": "{goalDictionary[goal][0]}"' + '}')

    # Write reversed function for Opponent goals
    elif 'N' in goal:
        file.write("execute as @s run function lockout:goals/skeleton/opponent {" + f'"goalid": "{goal}", "goalnum": "{ord(goal[0])}{number}", "goalname": "{goalDictionary[goal][0]}"' + '}')

    else:
        # Write goal triggers for all other goals
        file.write("execute as @s run function lockout:goals/skeleton/master {" + f'"goalid": "{goal}", "goalnum": "{ord(goal[0])}{number}", "goalname": "{goalDictionary[goal][0]}"' + '}')

    file.close()
