tellraw @s[tag=lk.N0012] {"text": "Your point for more kelp was removed due to disconnection."}
tellraw @s[tag=lk.N0013] {"text": "Your point for more hoppers was removed due to disconnection."}
tellraw @s[tag=lk.N0014] {"text": "Your point for more levels was removed due to disconnection."}

scoreboard players remove @s[tag=lk.N0012] lk.points 1
scoreboard players remove @s[tag=lk.N0013] lk.points 1
scoreboard players remove @s[tag=lk.N0014] lk.points 1

tag @s remove lk.N0012
tag @s remove lk.N0013
tag @s remove lk.N0014

