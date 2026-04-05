attribute @s jump_strength base set 0
attribute @s movement_speed base set 0
effect clear @s
effect give @s regeneration 3 10 true
effect give @s saturation 10 0 true
scoreboard players reset @s join_team

execute as @s run function lockout:game/reset/scoreboards_player
