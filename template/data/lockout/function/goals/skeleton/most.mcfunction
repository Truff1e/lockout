execute if score #end_seen lk.util matches 1 run return fail
execute if entity @s[predicate=!lockout:is_playing] run return fail

$scoreboard players set @s lk.goal $(goalnum)
execute as @s run function lockout:game/getgoal

$say completed "$(goalname)"
execute as @s[team=1] at @a[team=1] run playsound entity.player.levelup master @a[team=1] ~ ~ ~
execute as @s[team=2] at @a[team=2] run playsound entity.player.levelup master @a[team=2] ~ ~ ~
execute as @s[team=1] at @a[team=2] run playsound block.beacon.deactivate master @a[team=2] ~ ~ ~
execute as @s[team=2] at @a[team=1] run playsound block.beacon.deactivate master @a[team=1] ~ ~ ~

scoreboard players add @s lk.points 1
execute as @s[team=1] run scoreboard players add @e[tag=lk.team1pts] lk.points 1
execute as @s[team=2] run scoreboard players add @e[tag=lk.team2pts] lk.points 1
$execute if entity @s[team=1] as @a[tag=lk.$(goalid),team=2] run scoreboard players remove @e[tag=lk.team2pts] lk.points 1
$execute if entity @s[team=2] as @a[tag=lk.$(goalid),team=1] run scoreboard players remove @e[tag=lk.team1pts] lk.points 1
$execute if entity @s[team=1] as @a[tag=lk.$(goalid),team=1] run scoreboard players remove @e[tag=lk.team1pts] lk.points 1
$execute if entity @s[team=2] as @a[tag=lk.$(goalid),team=2] run scoreboard players remove @e[tag=lk.team2pts] lk.points 1
$execute as @a[tag=lk.$(goalid)] run scoreboard players remove @s lk.points 1

$tag @e remove lk.$(goalid)
$tag @e[tag=lk.goaltracker] add lk.$(goalid)
$execute as @s[team=1] run tag @e[tag=lk.team1pts] add lk.$(goalid)
$execute as @s[team=2] run tag @e[tag=lk.team2pts] add lk.$(goalid)
$tag @s add lk.$(goalid)