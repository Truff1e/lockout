execute if score #allow_pvp lk.util matches 1 run gamerule pvp true
gamerule advance_weather true
gamerule advance_time true

execute as @a run function lockout:game/reset/attributes
title @a title {"text": "Go!", "color": "dark_aqua"}
execute as @a at @s run playsound block.note_block.pling master @s ~ ~ ~ 1 2

scoreboard players set #state lk.util 2

#start loops
schedule function lockout:tick/1m 1s replace
schedule function lockout:tick/1s 1s replace
