tellraw @s[tag=lk.M0012] {"text": "Your point for most kelp was removed due to disconnection."}
tellraw @s[tag=lk.M0013] {"text": "Your point for most hoppers was removed due to disconnection."}
tellraw @s[tag=lk.M0014] {"text": "Your point for most levels was removed due to disconnection."}
tellraw @s[tag=lk.M0015] {"text": "Your point for most crafts was removed due to disconnection."}

scoreboard players remove @s[tag=lk.M0012] lk.points 1
scoreboard players remove @s[tag=lk.M0013] lk.points 1
scoreboard players remove @s[tag=lk.M0014] lk.points 1
scoreboard players remove @s[tag=lk.M0015] lk.points 1

tag @s remove lk.M0012
tag @s remove lk.M0013
tag @s remove lk.M0014
tag @s remove lk.M0015
