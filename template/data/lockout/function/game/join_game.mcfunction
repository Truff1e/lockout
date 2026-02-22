team join 1 @s[scores={join_team=1}]
team join 2 @s[scores={join_team=2}]
scoreboard players set @s join_team 0
gamemode survival @s
clear @s
kill @s
execute as @s run function lockout:game/reset_scoreboards
