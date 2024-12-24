execute if score #end_seen lk.util matches 1 run return fail
execute if entity @s[team=spectator] run return fail
execute store result score #dried_kelp lk.util run scoreboard players get @s lk.dried_kelp

scoreboard players set @s lk.goal 780012
execute as @s run function lockout:game/getgoal

say completed "Have the Most Dried Kelp Blocks"
execute as @s[team=1] at @a[team=1] run playsound entity.player.levelup master @a[team=1] ~ ~ ~
execute as @s[team=2] at @a[team=2] run playsound entity.player.levelup master @a[team=2] ~ ~ ~
execute as @s[team=1] at @a[team=2] run playsound block.beacon.deactivate master @a[team=2] ~ ~ ~
execute as @s[team=2] at @a[team=1] run playsound block.beacon.deactivate master @a[team=1] ~ ~ ~

scoreboard players add @s lk.stat.points 1
scoreboard players add @s lk.points 1
execute as @s[team=1] run scoreboard players add @e[tag=lk.team1pts] lk.points 1
execute as @s[team=2] run scoreboard players add @e[tag=lk.team2pts] lk.points 1
execute if entity @s[team=1] as @a[tag=lk.N0012,team=2] run scoreboard players remove @e[tag=lk.team2pts] lk.points 1
execute if entity @s[team=2] as @a[tag=lk.N0012,team=1] run scoreboard players remove @e[tag=lk.team1pts] lk.points 1
execute if entity @s[team=1] as @a[tag=lk.N0012,team=2] run scoreboard players remove @s lk.points 1
execute if entity @s[team=2] as @a[tag=lk.N0012,team=1] run scoreboard players remove @s lk.points 1
execute if entity @s[team=1] as @a[tag=lk.N0012,team=2] run scoreboard players remove @s lk.stat.points 1
execute if entity @s[team=2] as @a[tag=lk.N0012,team=1] run scoreboard players remove @s lk.stat.points 1

tag @a remove lk.N0012

#identifiers
tag @e[tag=lk.goaltracker] add lk.N0012
tag @s add lk.N0012