team join 1 @s[scores={join_team=1}]
team join 2 @s[scores={join_team=2}]
execute if score @s join_team matches 1 run say Joining Team 1
execute if score @s join_team matches 2 run say Joining Team 2
scoreboard players set @s join_team 0
gamemode survival @s
clear @s
kill @s
execute as @s run function lockout:game/reset_scoreboards
