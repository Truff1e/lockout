execute unless score #N0008 lk.enabled_goals matches 1 run return fail
execute if score #end_seen lk.util matches 1 run return fail
execute if entity @e[tag=lk.N0008] run return fail
execute if entity @s[team=spectator] run return fail
tag @s add lk.N0008
tag @e[tag=lk.goaltracker] add lk.N0008
scoreboard players set @s lk.goal 780008
execute as @s run function lockout:game/getgoal
execute as @s[team=2] run scoreboard players add @e[tag=lk.team1pts] lk.points 1
execute as @s[team=1] run scoreboard players add @e[tag=lk.team2pts] lk.points 1
say failed "Opponent Touches Water"
execute as @s[team=2] at @a[team=1] run playsound entity.player.levelup master @a[team=1] ~ ~ ~
execute as @s[team=1] at @a[team=2] run playsound entity.player.levelup master @a[team=2] ~ ~ ~
execute as @s[team=2] at @a[team=2] run playsound block.beacon.deactivate master @a[team=2] ~ ~ ~
execute as @s[team=1] at @a[team=1] run playsound block.beacon.deactivate master @a[team=1] ~ ~ ~
scoreboard players add @s lk.stat.failed_goals 1