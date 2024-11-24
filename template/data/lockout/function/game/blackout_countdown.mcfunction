attribute @s jump_strength base set 0
attribute @s movement_speed base set 0

scoreboard players set @a resign 0
scoreboard players set @a draw 0

execute if score #start_time lk.util matches 30 run title @s title {"text": "Blackout Will Start in 30 Seconds", "color": "dark_aqua"}
execute if score #start_time lk.util matches 45 run title @s title {"text": "Blackout Will Start in 45 Seconds", "color": "dark_aqua"}
execute if score #start_time lk.util matches 60 run title @s title {"text": "Blackout Will Start in 60 Seconds", "color": "dark_aqua"}
execute if score #start_time lk.util matches 90 run title @s title {"text": "Blackout Will Start in 90 Seconds", "color": "dark_aqua"}
execute if score #start_time lk.util matches 120 run title @s title {"text": "Blackout Will Start in 120 Seconds", "color": "dark_aqua"}

title @s subtitle [{"text": "Press ", "color": "aqua"}, {"keybind": "key.advancements", "color": "aqua"}, {"text":" for Blackout Board", "color": "aqua"}]

tellraw @s ["",{"text":"-----------","bold":true,"color":"dark_aqua"},{"text":" Minecraft Blackout","bold":true,"color":"aqua"},{"text":" -----------","bold":true,"color":"dark_aqua"},{"text":"\n\n"},{"text":"Objective:","bold":true,"color":"yellow"},{"text":" Complete every single\ngoal on the board.","color":"gold"},{"text":"\n\n"},{"text":"Press [","color":"light_purple"},{"keybind":"key.advancements","color":"light_purple"},{"text":"] to see the Blackout Board","color":"light_purple"},{"text":"\n\n"},{"text":"Type \"/trigger locate\" to see the location of\nother players.","color":"aqua"},{"text":"\n\n"},{"text":"Data Pack by Truffle, Game by SmallAnt","color":"gray"},{"text":"\n"},{"text":"©2024 - version 1.6.0 - MC1.21.3","italic":true,"color":"dark_gray"},{"text":" -------------","bold":true,"color":"dark_aqua"}]

effect give @s regeneration 3 10 true
effect give @s saturation 3 10 true

function lockout:game/reset_scoreboards

scoreboard players set #game_begun lk.util 1
scoreboard players set #test_effects lk.util 0

scoreboard players display name @e[type=armor_stand,tag=lk.team1pts] lk.points {"text":"Team 1","bold":true}
scoreboard players reset @e[type=armor_stand,tag=lk.team2pts] lk.points

time set day

execute if score #start_time lk.util matches 30 run function lockout:game/countdowns/30s
execute if score #start_time lk.util matches 45 run function lockout:game/countdowns/45s
execute if score #start_time lk.util matches 60 run function lockout:game/countdowns/60s
execute if score #start_time lk.util matches 90 run function lockout:game/countdowns/90s
execute if score #start_time lk.util matches 120 run function lockout:game/countdowns/120s