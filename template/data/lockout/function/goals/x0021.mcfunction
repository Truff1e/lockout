execute unless score #X0021 lk.enabled_goals matches 1 run return fail
execute if score #end_seen lk.util matches 1 run return fail
execute if entity @e[tag=lk.X0021] run return fail
execute if entity @s[team=spectator] run return fail
tag @s add lk.X0021
tag @e[tag=lk.goaltracker] add lk.X0021
scoreboard players set @s lk.goal 880021
execute as @s run function lockout:game/getgoal
execute as @s[team=1] run scoreboard players add @e[tag=lk.team1pts] lk.points 1
scoreboard players add @s lk.points 1
execute as @s[team=2] run scoreboard players add @e[tag=lk.team2pts] lk.points 1
say completed "Wash Leather Armor"
execute as @s[team=1] at @a[team=1] run playsound entity.player.levelup master @a[team=1] ~ ~ ~
execute as @s[team=2] at @a[team=2] run playsound entity.player.levelup master @a[team=2] ~ ~ ~
execute as @s[team=1] at @a[team=2] run playsound block.beacon.deactivate master @a[team=2] ~ ~ ~
execute as @s[team=2] at @a[team=1] run playsound block.beacon.deactivate master @a[team=1] ~ ~ ~
scoreboard players add @s lk.stat.points 1