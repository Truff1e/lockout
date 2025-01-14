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
        file.write('execute as @s run function lockout:goals/count_advancements\n')

    # Write reversed function for Opponent goals
    if 'N' in goal:
        if goal in have_more_goals:
            continue
        else:
            file.write(f'''execute unless score #{goal} lk.enabled_goals matches 1 run return fail
execute if score #end_seen lk.util matches 1 run return fail
execute if entity @e[tag=lk.{goal}] run return fail
execute if entity @s[team=spectator] run return fail
tag @s add lk.{goal}
tag @e[tag=lk.goaltracker] add lk.{goal}
scoreboard players set @s lk.goal {ord(goal[0])}{number}
execute as @s run function lockout:game/getgoal
execute as @s[team=2] run scoreboard players add @e[tag=lk.team1pts] lk.points 1
execute as @s[team=1] run scoreboard players add @e[tag=lk.team2pts] lk.points 1
say failed "{goalDictionary[goal][0]}"
execute as @s[team=2] at @a[team=1] run playsound entity.player.levelup master @a[team=1] ~ ~ ~
execute as @s[team=1] at @a[team=2] run playsound entity.player.levelup master @a[team=2] ~ ~ ~
execute as @s[team=2] at @a[team=2] run playsound block.beacon.deactivate master @a[team=2] ~ ~ ~
execute as @s[team=1] at @a[team=1] run playsound block.beacon.deactivate master @a[team=1] ~ ~ ~
scoreboard players add @s lk.stat.failed_goals 1''')
    else:
        # Write goal triggers for all other goals
        file.write(f'''execute unless score #{goal} lk.enabled_goals matches 1 run return fail
execute if score #end_seen lk.util matches 1 run return fail
execute if entity @e[tag=lk.{goal}] run return fail
execute if entity @s[team=spectator] run return fail
tag @s add lk.{goal}
tag @e[tag=lk.goaltracker] add lk.{goal}
scoreboard players set @s lk.goal {ord(goal[0])}{number}
execute as @s run function lockout:game/getgoal
execute as @s[team=1] run scoreboard players add @e[tag=lk.team1pts] lk.points 1
scoreboard players add @s lk.points 1
execute as @s[team=2] run scoreboard players add @e[tag=lk.team2pts] lk.points 1
say completed "{goalDictionary[goal][0]}"
execute as @s[team=1] at @a[team=1] run playsound entity.player.levelup master @a[team=1] ~ ~ ~
execute as @s[team=2] at @a[team=2] run playsound entity.player.levelup master @a[team=2] ~ ~ ~
execute as @s[team=1] at @a[team=2] run playsound block.beacon.deactivate master @a[team=2] ~ ~ ~
execute as @s[team=2] at @a[team=1] run playsound block.beacon.deactivate master @a[team=1] ~ ~ ~
''')

    file.close()
