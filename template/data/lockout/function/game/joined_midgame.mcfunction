team join spectator @s
gamemode spectator @s
execute if score #game_begun lk.util matches 1 run function lockout:game/resume

execute if score #blackout lk.util matches 1 run team join 1 @s
execute if score #blackout lk.util matches 1 run tellraw @s {"text":"Welcome! You have joined the Blackout game!"}
execute if score #blackout lk.util matches 1 run scoreboard players set @s join_team 1
execute if score #blackout lk.util matches 1 run return fail

scoreboard players enable @s join_team
tellraw @s {"text":"Welcome! You have joined in the middle of a Lockout game. Before joining a team, ask if you can play and which team you should join. Join a team with /trigger join_team <1/2>. This action is irreversible. Only an operator can switch your team once you join one."}
