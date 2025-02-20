#update timer
execute if score #game_begun lk.util matches 1 run function lockout:timer/timer

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
execute if score #show_progress lk.util matches 1 run scoreboard players enable @a progress

schedule function lockout:tick/1s 1s replace