execute unless entity @a[tag=lk.N0012] as @e[type=armor_stand,tag=lk.N0012,tag=!lk.goaltracker] run function lockout:goals/most/dried_kelp_logoff
execute unless entity @a[tag=lk.N0013] as @e[type=armor_stand,tag=lk.N0013,tag=!lk.goaltracker] run function lockout:goals/most/hoppers_logoff
execute unless entity @a[tag=lk.N0014] as @e[type=armor_stand,tag=lk.N0014,tag=!lk.goaltracker] run function lockout:goals/most/levels_logoff
execute if score #N0012 lk.enabled_goals matches 1 as @a run function lockout:goals/most/dried_kelp
execute if score #N0013 lk.enabled_goals matches 1 as @a run function lockout:goals/most/hoppers
execute if score #N0014 lk.enabled_goals matches 1 as @a run function lockout:goals/most/levels