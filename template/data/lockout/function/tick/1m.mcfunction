
scoreboard players add #game_time lk.util 1
scoreboard players operation #temp_max_time lk.util = #max_time lk.util
execute store result score #time_remaining lk.util run scoreboard players operation #temp_max_time lk.util -= #game_time lk.util
execute if score #game_time lk.util >= #max_time lk.util unless score #end_seen lk.util matches 1 run function lockout:game/time_out

execute if score #blackout lk.util matches 1 run scoreboard players reset @e[type=armor_stand,tag=lk.team2pts]

schedule function lockout:tick/1m 60s replace