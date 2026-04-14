#update timer
scoreboard players remove #seconds_remaining lk.util 1
function lockout:timer/timer

execute as @a[predicate=!lockout:is_playing, team=!spectator] run function lockout:game/joined_midgame
gamemode spectator @a[team=spectator]

#update scoreboards
execute as @a store result score @s lk.dried_kelp run clear @s dried_kelp_block 0
execute as @a store result score @s lk.hoppers run clear @s hopper 0

#TODO: clear effects from all players with resistance 5 so that players who log out during the start of the game dont keep effects

#run misc goal checks
function lockout:goals/other/scoreboard_goals
execute if predicate lockout:most/enabled run function lockout:goals/most/handler

#check for win
function lockout:game/detect_win

#reset scoreboards
scoreboard players set @a lk.logoff 0
scoreboard players set @a lk.death_trigger 0

#enable trigger commands
scoreboard players enable @a locate
scoreboard players enable @a resign
scoreboard players enable @a draw

execute as @a[scores={join_team=1..2}] run function lockout:game/join_game

execute if score #show_progress lk.util matches 1 run scoreboard players enable @a progress

schedule function lockout:tick/1s 1s replace
