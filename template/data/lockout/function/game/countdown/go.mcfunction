execute as @a run function lockout:game/reset_attributes
title @a title {"text": "Go!", "color": "dark_aqua"}
scoreboard players set #test_effects lk.util 1
execute at @a run playsound block.end_portal.spawn master @a ~ ~ ~

scoreboard players set #game_time lk.util 0

#start loops
schedule function lockout:tick/1m 1s replace
schedule function lockout:tick/1s 1s replace
