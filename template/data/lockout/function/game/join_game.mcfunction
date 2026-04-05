execute unless score #state lk.util matches 2 run return fail
team join 1 @s[scores={join_team=1}]
team join 2 @s[scores={join_team=2}]
execute if score @s join_team matches 1 run say joined Team 1
execute if score @s join_team matches 2 run say joined Team 2
scoreboard players reset @s join_team
gamemode survival @s
clear @s
kill @s
execute as @s run function lockout:game/reset/scoreboards_player
