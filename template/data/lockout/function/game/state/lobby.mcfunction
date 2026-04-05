execute unless score #state lk.util matches 0 run return fail

clear @s
effect give @s saturation infinite 0 true
scoreboard players enable @s join_team

execute as @s at @s unless entity @e[tag=lk.lobby] run function lockout:game/state/setup_lobby
execute if entity @e[tag=lk.lobby] run tp @s @e[tag=lk.lobby,limit=1,sort=nearest]

title @s title {"text":"Minecraft Lockout","color":"yellow"}
title @s subtitle {"text":"by Truffle","color":"yellow"}
execute at @s run playsound entity.player.levelup master @s ~ ~ ~ 1 1.2

tag @s add lk.initialized
