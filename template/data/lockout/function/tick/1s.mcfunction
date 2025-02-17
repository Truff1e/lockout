function lockout:goals/scoreboard_goals

scoreboard players remove #seconds_remaining lk.util 1

execute if score #game_begun lk.util matches 1 if score #time_remaining lk.util matches 1.. unless score #blackout lk.util matches 1 unless score #end_seen lk.util matches 1 run title @a actionbar [{"score":{"name": "@e[type=armor_stand,tag=lk.team1pts]", "objective": "lk.points"}, "color": "dark_purple"},{"text": " - ", "color": "gray"},{"score":{"name": "@e[type=armor_stand,tag=lk.team2pts]", "objective": "lk.points"}, "color": "dark_aqua"},{"text": "  |  ", "color": "gray"},{"score":{"name": "#time_remaining", "objective": "lk.util"}, "color": "yellow"},{"text": ":","color": "yellow"},{"score":{"name": "#seconds_remaining", "objective": "lk.util"}, "color": "yellow"}]

execute if score #game_begun lk.util matches 1 if score #time_remaining lk.util matches 1.. if score #blackout lk.util matches 1 unless score #end_seen lk.util matches 1 run title @a actionbar [{"score":{"name": "@e[type=armor_stand,tag=lk.team1pts]", "objective": "lk.points"}, "color": "dark_purple"},{"text": "/", "color": "gray"},{"score":{"name": "#boardSize", "objective": "lk.util"}, "color": "dark_purple"},{"text": "  |  ", "color": "gray"},{"score":{"name": "#time_remaining", "objective": "lk.util"}, "color": "yellow"},{"text": ":","color": "yellow"},{"score":{"name": "#seconds_remaining", "objective": "lk.util"}, "color": "yellow"}]

execute if score #game_begun lk.util matches 1 if score #time_remaining lk.util matches ..0 run title @a actionbar [{"text": "Game Over", "color": "red"}]
execute if score #end_seen lk.util matches 1 run title @a actionbar [{"text": "Game Finished", "color": "yellow"}]

execute if predicate lockout:most/enabled run function lockout:goals/most_goals

scoreboard players set @a lk.logoff 0

function lockout:game/detect_win

scoreboard players set @a lk.death_trigger 0
scoreboard players enable @a locate
scoreboard players enable @a resign
scoreboard players enable @a draw
execute if score #show_progress lk.util matches 1 run scoreboard players enable @a progress

schedule function lockout:tick/1s 1s replace