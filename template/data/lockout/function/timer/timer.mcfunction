scoreboard players remove #seconds_remaining lk.util 1

execute if score #time_remaining lk.util matches ..0 run title @a actionbar [{"text": "Game Over", "color": "red"}]
execute if score #end_seen lk.util matches 1 run title @a actionbar [{"text": "Game Finished", "color": "yellow"}]

execute if score #seconds_remaining lk.util matches ..9 run function lockout:timer/single_digit
execute if score #seconds_remaining lk.util matches ..9 run return fail

execute if score #time_remaining lk.util matches 1.. unless score #blackout lk.util matches 1 unless score #end_seen lk.util matches 1 run title @a actionbar [{"score":{"name": "@e[type=armor_stand,tag=lk.team1pts]", "objective": "lk.points"}, "color": "dark_purple"},{"text": " - ", "color": "gray"},{"score":{"name": "@e[type=armor_stand,tag=lk.team2pts]", "objective": "lk.points"}, "color": "dark_aqua"},{"text": "  |  ", "color": "gray"},{"score":{"name": "#time_remaining", "objective": "lk.util"}, "color": "yellow"},{"text": ":","color": "yellow"},{"score":{"name": "#seconds_remaining", "objective": "lk.util"}, "color": "yellow"}]

execute if score #time_remaining lk.util matches 1.. if score #blackout lk.util matches 1 unless score #end_seen lk.util matches 1 run title @a actionbar [{"score":{"name": "@e[type=armor_stand,tag=lk.team1pts]", "objective": "lk.points"}, "color": "dark_purple"},{"text": "/", "color": "gray"},{"score":{"name": "#boardSize", "objective": "lk.util"}, "color": "dark_purple"},{"text": "  |  ", "color": "gray"},{"score":{"name": "#time_remaining", "objective": "lk.util"}, "color": "yellow"},{"text": ":","color": "yellow"},{"score":{"name": "#seconds_remaining", "objective": "lk.util"}, "color": "yellow"}]