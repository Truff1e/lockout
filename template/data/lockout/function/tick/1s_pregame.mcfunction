execute as @a[tag=!lk.initialized,team=!spectator] run function lockout:game/pregame

team join 1 @a[scores={join_team=1}]
team join 2 @a[scores={join_team=2}]
scoreboard players set @a join_team 0

execute if score #game_begun lk.util matches 1 at @r[tag=lk.initialized] run fill ~20 310 ~20 ~-20 319 ~-20 air replace
execute if score #game_begun lk.util matches 1 run scoreboard players reset @s join_team

execute unless score #game_begun lk.util matches 1 run schedule function lockout:tick/1s_pregame 1s
