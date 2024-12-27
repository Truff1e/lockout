team add 1
team add 2
team add spectator
team modify 1 color dark_purple
team modify 2 color dark_aqua
team modify spectator color gray


scoreboard objectives add lk.util dummy
scoreboard objectives add lk.enabled_goals dummy
scoreboard objectives add lk.points dummy {"text": "Lockout", "color": "yellow", "bold": true}
scoreboard objectives setdisplay sidebar lk.points
scoreboard objectives add lk.goal dummy

scoreboard objectives add lk.logoff minecraft.custom:minecraft.leave_game

scoreboard objectives add lk.stat.failed_goals dummy
scoreboard objectives add lk.stat.deaths deathCount
scoreboard objectives add lk.stat.kills playerKillCount


##goals
scoreboard objectives add lk.unique_mobs dummy
scoreboard objectives add lk.unique_foods dummy
scoreboard objectives add lk.unique_breeds dummy
scoreboard objectives add lk.unique_advancements dummy
scoreboard objectives add lk.unique_flowers dummy
scoreboard objectives add lk.unique_saplings dummy
scoreboard objectives add lk.unique_trims dummy
scoreboard objectives add lk.unique_effects dummy
scoreboard objectives add lk.unique_logs dummy

scoreboard objectives add lk.levels level
scoreboard objectives add lk.hoppers dummy
scoreboard objectives add lk.dried_kelp dummy

scoreboard objectives add lk.pumpkin_head_timer dummy
scoreboard objectives add lk.sprint_1km minecraft.custom:minecraft.sprint_one_cm
scoreboard objectives add lk.use_anvil minecraft.used:minecraft.anvil
scoreboard objectives add lk.jump minecraft.custom:jump
scoreboard objectives add lk.mob_kills minecraft.custom:minecraft.mob_kills
scoreboard objectives add lk.mine_deepslate_diamond minecraft.mined:deepslate_diamond_ore
scoreboard objectives add lk.mine_diamond minecraft.mined:diamond_ore
scoreboard objectives add lk.mine_spawner minecraft.mined:spawner
scoreboard objectives add lk.mine_emerald minecraft.mined:emerald_ore
scoreboard objectives add lk.damage_taken minecraft.custom:damage_taken
scoreboard objectives add lk.death_count deathCount
scoreboard objectives add lk.death_trigger deathCount
scoreboard objectives add lk.hunger_bar food
scoreboard objectives add lk.armor_washed minecraft.custom:clean_armor
scoreboard objectives add lk.fall minecraft.custom:fall_one_cm
scoreboard objectives add lk.fall_dmg minecraft.custom:damage_taken


scoreboard objectives add lk.posX dummy
scoreboard objectives add lk.posZ dummy

scoreboard objectives add locate trigger
scoreboard objectives add resign trigger
scoreboard objectives add draw trigger

#settings
scoreboard players set #start_time lk.util 45
scoreboard players set #max_time lk.util 120
#constants
scoreboard players set #const_1 lk.util 1
scoreboard players set #const_2 lk.util 2

forceload add 0 0
execute unless entity @e[type=armor_stand,tag=lk.goaltracker] run summon minecraft:armor_stand 0 319 0 {NoGravity:1b,Marker:1b,Invisible:1b,Tags:["lk.goaltracker"]}
execute unless entity @e[type=armor_stand,tag=lk.team1pts] run summon minecraft:armor_stand 0 319 0 {NoGravity:1b,Marker:1b,Invisible:1b,Tags:["lk.team1pts"],CustomName:'"Team 1"'}
execute unless entity @e[type=armor_stand,tag=lk.team2pts] run summon minecraft:armor_stand 0 319 0 {NoGravity:1b,Marker:1b,Invisible:1b,Tags:["lk.team2pts"],CustomName:'"Team 2"'}


schedule function lockout:postload 1s
schedule function lockout:tick/1s 1s replace
schedule function lockout:tick/1m 1s replace