execute if score #end_seen lk.util matches 1 run return fail
execute if entity @s[team=spectator] run return fail

scoreboard players set @s lk.goal 780014
execute as @s run function lockout:game/getgoal

say completed "Have the Most Levels"
execute as @s[team=1] at @a[team=1] run playsound entity.player.levelup master @a[team=1] ~ ~ ~
execute as @s[team=2] at @a[team=2] run playsound entity.player.levelup master @a[team=2] ~ ~ ~
execute as @s[team=1] at @a[team=2] run playsound block.beacon.deactivate master @a[team=2] ~ ~ ~
execute as @s[team=2] at @a[team=1] run playsound block.beacon.deactivate master @a[team=1] ~ ~ ~

scoreboard players add @s lk.points 1
execute as @s[team=1] run scoreboard players add @e[tag=lk.team1pts] lk.points 1
execute as @s[team=2] run scoreboard players add @e[tag=lk.team2pts] lk.points 1
execute if entity @s[team=1] as @a[tag=lk.N0014,team=2] run scoreboard players remove @e[tag=lk.team2pts] lk.points 1
execute if entity @s[team=2] as @a[tag=lk.N0014,team=1] run scoreboard players remove @e[tag=lk.team1pts] lk.points 1
execute if entity @s[team=1] as @a[tag=lk.N0014,team=2] run scoreboard players remove @s lk.points 1
execute if entity @s[team=2] as @a[tag=lk.N0014,team=1] run scoreboard players remove @s lk.points 1

tag @e remove lk.N0014
tag @e[tag=lk.goaltracker] add lk.N0014
execute as @s[team=1] run tag @e[tag=lk.team1pts] add lk.N0014
execute as @s[team=2] run tag @e[tag=lk.team2pts] add lk.N0014
tag @s add lk.N0014