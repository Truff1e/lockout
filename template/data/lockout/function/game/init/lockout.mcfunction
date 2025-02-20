attribute @s jump_strength base set 0
attribute @s movement_speed base set 0

scoreboard players set @a resign 0
scoreboard players set @a draw 0

execute if score #start_time lk.util matches 30 run title @s title {"text": "Lockout Will Start in 30 Seconds", "color": "dark_aqua"}
execute if score #start_time lk.util matches 45 run title @s title {"text": "Lockout Will Start in 45 Seconds", "color": "dark_aqua"}
execute if score #start_time lk.util matches 60 run title @s title {"text": "Lockout Will Start in 60 Seconds", "color": "dark_aqua"}
execute if score #start_time lk.util matches 90 run title @s title {"text": "Lockout Will Start in 90 Seconds", "color": "dark_aqua"}
execute if score #start_time lk.util matches 120 run title @s title {"text": "Lockout Will Start in 120 Seconds", "color": "dark_aqua"}

title @s subtitle [{"text": "Press ", "color": "aqua"}, {"keybind": "key.advancements", "color": "aqua"}, {"text":" for Lockout Board", "color": "aqua"}]

tellraw @s ["",{"text":"======================================","color":"dark_gray"},{"text":"\n"},{"text":"Minecraft Lockout - by Truff1e","bold":true,"color":"yellow"},{"text":"\n\n"},{"text":"Objective: Complete more than half of the\ngoals on the board. If the other team gets\na goal, you can no longer get that goal.","color":"yellow"},{"text":"\n\n"},{"text":">> Press [","color":"green"},{"keybind":"key.advancements","color":"green"},{"text":"] to see the Lockout Board","color":"green"},{"text":"\n"},{"text":">> Type '/trigger locate' to see other\nplayers' locations. (Effectively a compass)","color":"aqua"},{"text":"\n\n"},{"text":"©2024 - MCfunction Development","italic":true,"color":"gray"},{"text":"\n"},{"text":"======================================","color":"dark_gray"}]

effect give @s regeneration 3 10 true
effect give @s saturation 3 10 true

function lockout:game/reset_scoreboards

scoreboard players set #game_begun lk.util 1
scoreboard players set #test_effects lk.util 0

scoreboard players display name @e[type=armor_stand,tag=lk.team1pts] lk.points {"text":"Team 1","bold":true}
scoreboard players display name @e[type=armor_stand,tag=lk.team2pts] lk.points {"text":"Team 2","bold":true}

time set day

execute if score #start_time lk.util matches 15 run function lockout:game/countdowns/15s
execute if score #start_time lk.util matches 30 run function lockout:game/countdowns/30s
execute if score #start_time lk.util matches 45 run function lockout:game/countdowns/45s
execute if score #start_time lk.util matches 60 run function lockout:game/countdowns/60s
execute if score #start_time lk.util matches 90 run function lockout:game/countdowns/90s
execute if score #start_time lk.util matches 120 run function lockout:game/countdowns/120s