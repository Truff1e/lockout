team join 1 @e[tag=lk.team1pts]
team join 2 @e[tag=lk.team2pts]
#execute unless entity @e[type=armor_stand,tag=lk.team1pts] run scoreboard players display name @e[type=armor_stand,tag=lk.team1pts] lk.points {"text":"Team 1","bold":true}
#execute unless entity @e[type=armor_stand,tag=lk.team2pts] run scoreboard players display name @e[type=armor_stand,tag=lk.team2pts] lk.points {"text":"Team 2","bold":true}
tellraw @a ["",{"text":"---------------------------","color":"gray"},{"text":"\n"},{"text":"Lockout Loaded Successfully!","bold":true,"color":"light_purple"},{"text":"\n\n"},{"text":"Data Pack by Truff1e","color":"dark_purple"},{"text":"\n"},{"text":"Game by SmallAnt","color":"dark_red"},{"text":"\n\n"},{"text":"DP Version - 1.7.1\nMC Version - 1.21.4","color":"gray"},{"text":"\n"},{"text":"---------------------------","color":"gray"}]
tellraw @a ["",{"text": ">>> START LOCKOUT", "color": "green","clickEvent": {"action": "suggest_command","value": "/function lockout:game/start"}}]
tellraw @a ["",{"text": ">>> START BLACKOUT", "color": "aqua","clickEvent": {"action": "suggest_command","value": "/function lockout:game/start_blackout"}}]
tellraw @a ["",{"text": ">>> SHOW TIME SETTINGS", "color": "gray","clickEvent": {"action": "suggest_command","value": "/function lockout:menu"}}]