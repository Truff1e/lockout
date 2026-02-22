execute if score #game_begun lk.util matches 1 run return fail
clear @s
effect give @s resistance infinite 4 true
scoreboard players enable @s join_team

execute at @s unless entity @a[tag=lk.initialized] run fill ~5 310 ~5 ~-5 317 ~-5 barrier replace air hollow
execute at @s run tp @s ~ 315 ~
execute if entity @p[tag=lk.initialized] run tp @s @p[tag=lk.initialized]

tag @s add lk.initialized
