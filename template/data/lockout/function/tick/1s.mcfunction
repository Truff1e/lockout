function lockout:goals/scoreboard_goals

execute if score #game_begun lk.util matches 1 if score #time_remaining lk.util matches 1.. unless score #blackout lk.util matches 1 unless score #end_seen lk.util matches 1 run title @a actionbar [{"score":{"name": "@e[type=armor_stand,tag=lk.team1pts]", "objective": "lk.points"}, "color": "dark_purple"},{"text": " - ", "color": "gray"},{"score":{"name": "@e[type=armor_stand,tag=lk.team2pts]", "objective": "lk.points"}, "color": "dark_aqua"},{"text": "  |  ", "color": "gray"},{"score":{"name": "#time_remaining", "objective": "lk.util"}, "color": "yellow"},{"text": " minutes","color": "yellow"}]

execute if score #game_begun lk.util matches 1 if score #time_remaining lk.util matches 1.. if score #blackout lk.util matches 1 unless score #end_seen lk.util matches 1 run title @a actionbar [{"score":{"name": "@e[type=armor_stand,tag=lk.team1pts]", "objective": "lk.points"}, "color": "dark_purple"},{"text": "/", "color": "gray"},{"score":{"name": "#boardSize", "objective": "lk.util"}, "color": "dark_purple"},{"text": "  |  ", "color": "gray"},{"score":{"name": "#time_remaining", "objective": "lk.util"}, "color": "yellow"},{"text": " minutes","color": "yellow"}]

execute if score #game_begun lk.util matches 1 if score #time_remaining lk.util matches ..0 run title @a actionbar [{"text": "Game Ended", "color": "red"}]
execute if score #end_seen lk.util matches 1 run title @a actionbar [{"text": "Game Ended", "color": "red"}]

execute as @a store result score @s lk.dried_kelp run clear @s dried_kelp_block 0
execute as @a store result score @s lk.hoppers run clear @s hopper 0

function lockout:goals/most_goals

scoreboard players set @a lk.logoff 0

function lockout:game/detect_win

scoreboard players set @a lk.death_trigger 0
scoreboard players enable @a locate
scoreboard players enable @a resign
scoreboard players enable @a draw

schedule function lockout:tick/1s 1s replace