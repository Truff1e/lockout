execute as @a store result score @s lk.dried_kelp run clear @s dried_kelp_block 0
execute as @a store result score @s lk.hoppers run clear @s hopper 0

execute if score #N0012 lk.enabled_goals matches 1 as @a run function lockout:goals/dried_kelp
execute if score #N0013 lk.enabled_goals matches 1 as @a run function lockout:goals/hoppers
execute if score #N0016 lk.enabled_goals matches 1 as @a run function lockout:goals/levels


schedule function lockout:tick/5s 5s replace