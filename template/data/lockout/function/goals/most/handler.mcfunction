#update scoreboards
execute as @a store result score @s lk.dried_kelp run clear @s dried_kelp_block 0
execute as @a store result score @s lk.hoppers run clear @s hopper 0

#handle logoffs
execute unless entity @a[tag=lk.M0012] as @e[type=armor_stand,tag=lk.M0012,tag=!lk.goaltracker] run function lockout:goals/most/logoff {"goalid": "M0012", "type": "dried kelp"}
execute unless entity @a[tag=lk.M0013] as @e[type=armor_stand,tag=lk.M0013,tag=!lk.goaltracker] run function lockout:goals/most/logoff {"goalid": "M0013", "type": "hoppers"}
execute unless entity @a[tag=lk.M0014] as @e[type=armor_stand,tag=lk.M0014,tag=!lk.goaltracker] run function lockout:goals/most/logoff {"goalid": "M0014", "type": "levels"}
execute unless entity @a[tag=lk.M0015] as @e[type=armor_stand,tag=lk.M0015,tag=!lk.goaltracker] run function lockout:goals/most/logoff {"goalid": "M0015", "type": "unique crafts"}

#check for new highest player
#execute as @a[predicate=lockout:most/unique_crafts] run say Predicate most unique crafts passed
#execute as @a[predicate=lockout:most/unique_crafts] if score @s lk.unique_crafts > #unique_crafts lk.util run say Second check passed
execute if score #M0012 lk.enabled_goals matches 1 as @a[predicate=lockout:most/dried_kelp,limit=1,sort=random,tag=!lk.M0012] if score @s lk.dried_kelp > #dried_kelp lk.dried_kelp run function lockout:goals/n0012
execute if score #M0013 lk.enabled_goals matches 1 as @a[predicate=lockout:most/hoppers,limit=1,sort=random,tag=!lk.M0013] if score @s lk.hoppers > #hoppers lk.hoppers run function lockout:goals/n0013
execute if score #M0014 lk.enabled_goals matches 1 as @a[predicate=lockout:most/levels,limit=1,sort=random,tag=!lk.M0014] if score @s lk.levels > #levels lk.util run function lockout:goals/n0014
execute if score #M0015 lk.enabled_goals matches 1 as @a[predicate=lockout:most/unique_crafts,limit=1,sort=random,tag=!lk.M0015] if score @s lk.unique_crafts > #unique_crafts lk.util run function lockout:goals/n0015

#decrement placeholder until next highest player found
#store current highest value in placeholder
execute unless entity @a[tag=lk.M0012] unless score #dried_kelp lk.dried_kelp matches ..0 run scoreboard players remove #dried_kelp lk.dried_kelp 1
execute if entity @a[tag=lk.M0012] store result score #dried_kelp lk.dried_kelp run scoreboard players get @a[tag=lk.M0012,limit=1] lk.dried_kelp

execute unless entity @a[tag=lk.M0013] unless score #hoppers lk.hoppers matches ..0 run scoreboard players remove #hoppers lk.hoppers 1
execute if entity @a[tag=lk.M0013] store result score #hoppers lk.hoppers run scoreboard players get @a[tag=lk.M0013,limit=1] lk.hoppers

execute unless entity @a[tag=lk.M0014] unless score #levels lk.util matches ..0 run scoreboard players remove #levels lk.util 1
execute if entity @a[tag=lk.M0014] store result score #levels lk.util run scoreboard players get @a[tag=lk.M0014,limit=1] lk.levels

execute unless entity @a[tag=lk.M0015] unless score #unique_crafts lk.util matches ..10 run scoreboard players remove #unique_crafts lk.util 1
execute if entity @a[tag=lk.M0015] store result score #unique_crafts lk.util run scoreboard players get @a[tag=lk.M0015,limit=1] lk.unique_crafts
