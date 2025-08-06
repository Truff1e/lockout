#team scorebaord entities
forceload add 0 0
execute unless entity @e[type=armor_stand,tag=lk.goaltracker] run summon minecraft:armor_stand 0 319 0 {NoGravity:1b,Marker:1b,Invisible:1b,Tags:["lk.goaltracker"]}
execute unless entity @e[type=armor_stand,tag=lk.team1pts] run summon minecraft:armor_stand 0 319 0 {NoGravity:1b,Marker:1b,Invisible:1b,Tags:["lk.team1pts"],CustomName:'"Team 1"'}
execute unless entity @e[type=armor_stand,tag=lk.team2pts] run summon minecraft:armor_stand 0 319 0 {NoGravity:1b,Marker:1b,Invisible:1b,Tags:["lk.team2pts"],CustomName:'"Team 2"'}

team join 1 @e[tag=lk.team1pts]
team join 2 @e[tag=lk.team2pts]

tellraw @a ["",{"text":"======================================","color":"dark_gray"},{"text":"\n"},{"text":"Minecraft Lockout  |  v2.0  |  1.21.8 ","bold":true,"color":"yellow"},{"text":"\n"},{"text":"Concept by SmallAnt, Developed by Truff1e","italic":true,"color":"yellow"},{"text":"\n\n"},{"text":">> Play Lockout","color":"light_purple","click_event":{"action":"suggest_command","command":"/function lockout:game/start"}},{"text":"\n"},{"text":">> Play Blackout","color":"light_purple","click_event":{"action":"suggest_command","command":"/function lockout:game/start_blackout"}},{"text":"\n"},{"text":">> Settings","color":"aqua","click_event":{"action":"suggest_command","command":"/function lockout:menu"}},{"text":"\n\n"},{"text":"©2025 - Truff1e","italic":true,"color":"gray"},{"text":"\n"},{"text":"======================================","color":"dark_gray"}]
