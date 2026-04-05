execute at @e[tag=lk.lobby] run fill ~20 310 ~20 ~-20 319 ~-20 air replace
scoreboard players reset @s join_team
kill @e[tag=lk.lobby]

execute as @a run function lockout:game/state/pregame
scoreboard players set @a resign 0
scoreboard players set @a draw 0

# Reset Scoreboards
function lockout:game/reset/scoreboards_most
scoreboard players set #state lk.util 1

execute unless score #blackout lk.util matches 1 as @s run function lockout:game/init_lockout
execute if score #blackout lk.util matches 1 run function lockout:game/init_blackout

execute store result storage minecraft:macro countdown.time int 1 run scoreboard players get #start_time lk.util
function lockout:game/countdown/start with storage minecraft:macro countdown

schedule function lockout:tick/1s_pregame 1s replace
