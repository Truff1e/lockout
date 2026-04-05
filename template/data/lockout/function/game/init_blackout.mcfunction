title @s title [{"text": "Blackout Will Start in ", "color": "dark_aqua"},{"score":{"name": "#start_time", "objective":"lk.util"}, "color":"dark_aqua"},{"text":" Seconds", "color":"dark_aqua"}]
title @s subtitle [{"text": "Press [", "color": "aqua"}, {"keybind": "key.advancements", "color": "aqua"}, {"text":"] to see the board", "color": "aqua"}]
tellraw @s ["",{"text":"========================================","color":"dark_gray"},{"text":"\n"},{"text":"Minecraft Blackout","bold":true,"color":"yellow"},{"text":"\n\n"},{"text":"Objective: Complete all of the goals on the\nboard before the time runs out.","color":"yellow"},{"text":"\n\n"},{"text":">> Press [","color":"green"},{"keybind":"key.advancements","color":"green"},{"text":"] to see the Blackout Board","color":"green"},{"text":"\n"},{"text":"\n©2025 - Truff1e","italic":true,"color":"gray"},{"text":"\n========================================","color":"dark_gray"}]

scoreboard objectives modify lk.points displayname {"text": "Blackout", "color": "yellow", "bold": true}
scoreboard players display name @e[type=armor_stand,tag=lk.team1pts] lk.points {"text":"Total","bold":true,"color": "dark_purple"}
