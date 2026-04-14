execute as @a[tag=!lk.initialized,team=!spectator] run function lockout:game/state/lobby

team join 1 @a[scores={join_team=1}]
tellraw @a[scores={join_team=1}] {"text":"Joined team 1", "color": "dark_purple"}
team join 2 @a[scores={join_team=2}]
tellraw @a[scores={join_team=2}] {"text":"Joined team 2", "color": "dark_aqua"}
team join spectator @a[scores={join_team=3..}]
tellraw @a[scores={join_team=3}] {"text":"Joined spectators", "color": "gray"}
scoreboard players set @a join_team 0
scoreboard players enable @a join_team

execute if score #state lk.util matches 1.. run function lockout:game/set_state/pregame
execute unless score #state lk.util matches 1.. run schedule function lockout:tick/1s_lobby 1s
