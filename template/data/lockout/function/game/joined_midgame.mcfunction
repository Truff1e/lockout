team join spectator @s
gamemode spectator @s
execute if score #game_begun lk.util matches 1 run function lockout:game/resume
scoreboard players enable @s join_team
tellraw @s {"text":"Welcome to the lockout game! Join a team with /trigger join_team <1/2>. Joining a team will kill you!"}
