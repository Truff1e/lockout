
scoreboard players set #seconds_remaining lk.util 60
scoreboard players add #game_time lk.util 1
execute store result score #temp_max_time lk.util run scoreboard players get #max_time lk.util
execute store result score #time_remaining lk.util run scoreboard players operation #temp_max_time lk.util -= #game_time lk.util

execute if score #time_remaining lk.util matches ..-1 unless score #end_seen lk.util matches 1 run function lockout:game/end/time_out

schedule function lockout:tick/1m 60s replace
