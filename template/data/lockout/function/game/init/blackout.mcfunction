attribute @s jump_strength base set 0
attribute @s movement_speed base set 0

scoreboard players set @a resign 0
scoreboard players set @a draw 0

title @s title [{"text": "Blackout Will Start in ", "color": "dark_aqua"},{"score":{"name": "#start_time", "objective":"lk.util"}, "color":"dark_aqua"},{"text":" Seconds", "color":"dark_aqua"}]
title @s subtitle [{"text": "Press ", "color": "aqua"}, {"keybind": "key.advancements", "color": "aqua"}, {"text":" for Blackout Board", "color": "aqua"}]

scoreboard objectives modify lk.points displayname {"text": "Blackout", "color": "yellow", "bold": true}

tellraw @s ["",{"text":"========================================","color":"dark_gray"},{"text":"\n"},{"text":"Minecraft Blackout","bold":true,"color":"yellow"},{"text":"\n"},{"text":"Objective: Complete all of the goals on the\nboard before the time runs out.","color":"yellow"},{"text":"\n\n"},{"text":">> Press [","color":"green"},{"keybind":"key.advancements","color":"green"},{"text":"] to see the Blackout Board","color":"green"},{"text":"\n"},{"text":"©2025 - Truff1e","italic":true,"color":"gray"},{"text":"========================================","color":"dark_gray"}]

effect give @s regeneration 3 10 true
effect give @s saturation 3 10 true

function lockout:game/reset_scoreboards

scoreboard players set #game_begun lk.util 1
scoreboard players set #test_effects lk.util 0

#scoreboard players display name @e[type=armor_stand,tag=lk.team1pts] lk.points {"text":"Team 1","bold":true}
#scoreboard players reset @e[type=armor_stand,tag=lk.team2pts] lk.points

time set day

execute store result storage minecraft:macro countdown.time int 1 run scoreboard players get #start_time lk.util
function lockout:game/countdown/init with storage minecraft:macro countdown
