
scoreboard players set #seconds_remaining lk.util 60
scoreboard players add #game_time lk.util 1
execute store result score #temp_max_time lk.util run scoreboard players get #max_time lk.util
execute store result score #time_remaining lk.util run scoreboard players operation #temp_max_time lk.util -= #game_time lk.util

execute if score #time_remaining lk.util matches ..-1 unless score #state lk.util matches 3 run function lockout:game/set_state/end {"reason": "Time Elapsed", "message": "Game Over", "color":"gray"}

schedule function lockout:tick/1m 60s replace
