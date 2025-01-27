execute as @a store result score @s lk.dried_kelp run clear @s dried_kelp_block 0
execute as @a store result score @s lk.hoppers run clear @s hopper 0

execute unless entity @a[tag=lk.N0012] as @e[type=armor_stand,tag=lk.N0012,tag=!lk.goaltracker] run function lockout:goals/most/dried_kelp_logoff
execute unless entity @a[tag=lk.N0013] as @e[type=armor_stand,tag=lk.N0013,tag=!lk.goaltracker] run function lockout:goals/most/hoppers_logoff
execute unless entity @a[tag=lk.N0014] as @e[type=armor_stand,tag=lk.N0014,tag=!lk.goaltracker] run function lockout:goals/most/levels_logoff

execute if score #N0012 lk.enabled_goals matches 1 as @a[predicate=lockout:most/dried_kelp,limit=1,sort=random,tag=!lk.N0012] if score @s lk.dried_kelp > #dried_kelp lk.dried_kelp run function lockout:goals/n0012
execute if score #N0013 lk.enabled_goals matches 1 as @a[predicate=lockout:most/hoppers,limit=1,sort=random,tag=!lk.N0013] if score @s lk.hoppers > #hoppers lk.hoppers run function lockout:goals/n0013
execute if score #N0014 lk.enabled_goals matches 1 as @a[predicate=lockout:most/levels,limit=1,sort=random,tag=!lk.N0014] if score @s lk.levels > #levels lk.levels run function lockout:goals/n0014

execute unless entity @a[tag=lk.N0012] unless score #dried_kelp lk.dried_kelp matches ..0 run scoreboard players remove #dried_kelp lk.dried_kelp 1
execute if entity @a[tag=lk.N0012] store result score #dried_kelp lk.dried_kelp run scoreboard players get @a[tag=lk.N0012,limit=1] lk.dried_kelp

execute unless entity @a[tag=lk.N0013] unless score #hoppers lk.hoppers matches ..0 run scoreboard players remove #hoppers lk.hoppers 1
execute if entity @a[tag=lk.N0013] store result score #hoppers lk.hoppers run scoreboard players get @a[tag=lk.N0013,limit=1] lk.hoppers

execute unless entity @a[tag=lk.N0014] unless score #levels lk.levels matches ..0 run scoreboard players remove #levels lk.levels 1
execute if entity @a[tag=lk.N0014] store result score #levels lk.levels run scoreboard players get @a[tag=lk.N0014,limit=1] lk.levels