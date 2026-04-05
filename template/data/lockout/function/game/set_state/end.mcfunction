$tellraw @a {"text":"$(message)", "color":"$(color)"}
$tellraw @a {"text":"$(reason)", "color":"gray"}
$title @a title {"text":"$(message)","color":"$(color)"}
$title @a subtitle {"text":"$(reason)","color":"gray"}

execute as @a at @s run playsound entity.ender_dragon.death master @s ~ ~ ~
gamemode spectator @a

scoreboard players set @a resign 0
scoreboard players set @a draw 0
scoreboard players remove #game_time lk.util 1


tellraw @a {"text": "========================================", "color": "gray"}
$tellraw @a {"text": "Game Over - $(reason)", "bold": true, "color": "yellow"}
tellraw @a [{"text": "Team 1: ", "color":"dark_purple"},{"score": {"name": "@e[type=armor_stand,tag=lk.team1pts]", "objective": "lk.points"}}]
tellraw @a [{"text": "Team 2: ", "color":"dark_aqua"},{"score": {"name": "@e[type=armor_stand,tag=lk.team2pts]", "objective": "lk.points"}}]
tellraw @a [{"text": "Max Time: ", "color":"gold"},{"score": {"name": "#max_time", "objective": "lk.util"}},{"text": "min"}]
tellraw @a [{"text": "Game Length: ", "color":"gold"},{"score": {"name": "#game_time", "objective": "lk.util"}},{"text": "min"}]
tellraw @a {"text": "\n"}
tellraw @a {"text": "Player Stats", "bold": true, "color": "light_purple"}
tellraw @a {"text": "----------------------------------------", "color": "gray"}

execute as @a run function lockout:game/stats/global
scoreboard players set #state lk.util 3
tellraw @a {"text": "========================================", "color": "gray"}
function lockout:game/stats/export

schedule function lockout:tick/1s 1s replace
