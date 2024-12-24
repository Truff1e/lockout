scoreboard players remove @s[tag=lk.N0012] lk.points 1
scoreboard players remove @s[tag=lk.N0013] lk.points 1
scoreboard players remove @s[tag=lk.N0014] lk.points 1

tag @s remove lk.N0012
tag @s remove lk.N0013
tag @s remove lk.N0014

tellraw @s {"text": "Your point for more kelp/hoppers/levels was removed due to disconnection."}