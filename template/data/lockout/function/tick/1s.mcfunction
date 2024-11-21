execute as @a[scores={locate=1..}] run function lockout:locate
execute as @a[scores={lk.levels=30}] run function lockout:goals/x0001
#execute as @a[scores={lk.jump=1..3}] run function lockout:goals/n0005
execute as @a[scores={lk.mob_kills=100..110}] run function lockout:goals/k0001
execute as @a[scores={lk.mine_deepslate_diamond=1..3}] run function lockout:goals/x0007
execute as @a[scores={lk.mine_diamond=1..3}] run function lockout:goals/x0007
execute as @a[scores={lk.mine_emerald=1..3}] run function lockout:goals/x0012
execute as @a[scores={lk.mine_spawner=1..3}] run function lockout:goals/x0008
execute as @a[scores={lk.sprint_1km=100000..150000}] run function lockout:goals/x0009
execute as @a[scores={lk.damage_taken=1000..2000}] run function lockout:goals/n0010
execute as @a[scores={lk.damage_taken=2000..3000}] run function lockout:goals/x0018
execute as @a[scores={lk.death_count=1}] run function lockout:goals/n0001
execute as @a[scores={lk.death_trigger=1}] at @s if block ~ ~ ~ pointed_dripstone run function lockout:goals/d0007
execute as @a[scores={lk.death_count=3}] run function lockout:goals/n0011
execute as @a[scores={lk.hunger_bar=0}] run function lockout:goals/x0020
execute as @a[predicate=lockout:on_fire] run function lockout:goals/n0004
execute as @a[scores={lk.armor_washed=1..4}] run function lockout:goals/x0021
execute as @a[predicate=lockout:pumpkin_head] run scoreboard players add @s lk.pumpkin_head_timer 1
execute as @a[predicate=!lockout:pumpkin_head] run scoreboard players set @s lk.pumpkin_head_timer 0
execute as @a[scores={lk.pumpkin_head_timer=300..}] run function lockout:goals/x0014
#execute as @a[scores={lk.fall=400..,lk.fall_dmg=2..}] run function lockout:goals/n0003

scoreboard players enable @a locate
scoreboard players enable @a resign
scoreboard players enable @a draw

execute if score #game_begun lk.util matches 1 if score #time_remaining lk.util matches 1.. run title @a actionbar [{"text": "Time Remaining: ", "color": "light_purple"},{"score":{"name": "#time_remaining", "objective": "lk.util"}, "color": "light_purple"},{"text": " minutes","color": "light_purple"}]

execute if score #game_begun lk.util matches 1 if score #time_remaining lk.util matches ..0 run title @a actionbar [{"text": "Game Ended", "color": "red"}]

execute as @a[scores={lk.logoff=1..}] if score #game_begun lk.util matches 1 run function lockout:game/resume
scoreboard players set @a lk.logoff 0


execute as @e[type=armor_stand,tag=lk.team1pts] if score @s lk.points >= #boardSize lk.util unless score #end_seen lk.util matches 1 run function lockout:game/win
execute as @e[type=armor_stand,tag=lk.team2pts] if score @s lk.points >= #boardSize lk.util unless score #end_seen lk.util matches 1 run function lockout:game/win
execute as @r[scores={resign=1..}, team=1] unless entity @a[scores={resign=0}, team=1] run function lockout:game/resign
execute as @r[scores={resign=1..}, team=2] unless entity @a[scores={resign=0}, team=2] run function lockout:game/resign
execute as @r[scores={draw=1..}] unless entity @a[scores={draw=0}, team=!spectator] run function lockout:game/draw

scoreboard players set @a lk.death_trigger 0

schedule function lockout:tick/1s 1s replace