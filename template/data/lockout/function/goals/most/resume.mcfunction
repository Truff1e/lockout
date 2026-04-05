execute unless score #state lk.util matches 2 run return fail

tellraw @s[tag=lk.M0006] {"text": "[Lockout] Your goal for most deaths was removed because you disconnected"}
tellraw @s[tag=lk.M0007] {"text": "[Lockout] Your goal for most advancements was removed because you disconnected"}
tellraw @s[tag=lk.M0008] {"text": "[Lockout] Your goal for most unique breeds was removed because you disconnected"}
tellraw @s[tag=lk.M0009] {"text": "[Lockout] Your goal for most unique foods was removed because you disconnected"}
tellraw @s[tag=lk.M0010] {"text": "[Lockout] Your goal for most unique trims was removed because you disconnected"}
tellraw @s[tag=lk.M0011] {"text": "[Lockout] Your goal for most unique mobs was removed because you disconnected"}
tellraw @s[tag=lk.M0012] {"text": "[Lockout] Your goal for most dried kelp was removed because you disconnected"}
tellraw @s[tag=lk.M0013] {"text": "[Lockout] Your goal for most hoppers was removed becuase you disconnected"}
tellraw @s[tag=lk.M0014] {"text": "[Lockout] Your goal for most levels was removed because you disconnected"}
tellraw @s[tag=lk.M0015] {"text": "[Lockout] Your goal for most crafts was removed because you disconnected"}

scoreboard players remove @s[tag=lk.M0006] lk.points 1
scoreboard players remove @s[tag=lk.M0007] lk.points 1
scoreboard players remove @s[tag=lk.M0008] lk.points 1
scoreboard players remove @s[tag=lk.M0009] lk.points 1
scoreboard players remove @s[tag=lk.M0010] lk.points 1
scoreboard players remove @s[tag=lk.M0011] lk.points 1
scoreboard players remove @s[tag=lk.M0012] lk.points 1
scoreboard players remove @s[tag=lk.M0013] lk.points 1
scoreboard players remove @s[tag=lk.M0014] lk.points 1
scoreboard players remove @s[tag=lk.M0015] lk.points 1

tag @s remove lk.M0006
tag @s remove lk.M0007
tag @s remove lk.M0008
tag @s remove lk.M0009
tag @s remove lk.M0010
tag @s remove lk.M0011
tag @s remove lk.M0012
tag @s remove lk.M0013
tag @s remove lk.M0014
tag @s remove lk.M0015
