execute as @a run function lockout:game/reset_attributes
title @a title {"text": "Go!", "color": "dark_aqua"}
scoreboard players set #game_time lk.util 0
scoreboard players set #test_effects lk.util 1
execute at @a run playsound block.end_portal.spawn master @a ~ ~ ~