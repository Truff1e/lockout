#trigger functions
execute as @a[scores={locate=1..}] run function lockout:trigger/locate
execute as @a[scores={progress=1..}] run function lockout:trigger/progress

#goals
execute as @a[scores={lk.levels=30}] run function lockout:goals/x0001
execute as @a[scores={lk.levels=15}] run function lockout:goals/x0025
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
execute as @a[predicate=lockout:on_fire,predicate=!lockout:effects/fire_resistance] run function lockout:goals/n0004
execute as @a[scores={lk.armor_washed=1..4}] run function lockout:goals/x0021
execute as @a[predicate=lockout:pumpkin_head] run scoreboard players add @s lk.pumpkin_head_timer 1
execute as @a[predicate=!lockout:pumpkin_head] run scoreboard players set @s lk.pumpkin_head_timer 0
execute as @a[scores={lk.pumpkin_head_timer=300..}] run function lockout:goals/x0014