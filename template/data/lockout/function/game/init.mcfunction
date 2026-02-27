attribute @s jump_strength base set 0
attribute @s movement_speed base set 0
effect clear @s
effect give @s regeneration 3 10 true
effect give @s saturation 3 10 true

scoreboard players set @a resign 0
scoreboard players set @a draw 0

execute as @a run function lockout:game/reset_scoreboards
scoreboard players set #dried_kelp lk.dried_kelp 0
scoreboard players set #hoppers lk.hoppers 0
scoreboard players set #levels lk.util 0
scoreboard players set #unique_crafts lk.util 10
scoreboard players set #game_begun lk.util 1
scoreboard players set #test_effects lk.util 0


execute unless score #blackout lk.util matches 1 as @s run function lockout:game/init_lockout
execute if score #blackout lk.util matches 1 run function lockout:game/init_blackout
title @s subtitle [{"text": "Press [", "color": "aqua"}, {"keybind": "key.advancements", "color": "aqua"}, {"text":"] To See Goals", "color": "aqua"}]

time set day

execute store result storage minecraft:macro countdown.time int 1 run scoreboard players get #start_time lk.util
function lockout:game/countdown/start with storage minecraft:macro countdown
