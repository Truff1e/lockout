execute unless entity @a[tag=lk.N0012] unless score #dried_kelp lk.dried_kelp matches ..0 run scoreboard players remove #dried_kelp lk.dried_kelp 1
execute if entity @a[tag=lk.N0012] store result score #dried_kelp lk.dried_kelp run scoreboard players get @a[tag=lk.N0012,limit=1] lk.dried_kelp

execute unless entity @a[tag=lk.N0013] unless score #hoppers lk.hoppers matches ..0 run scoreboard players remove #hoppers lk.hoppers 1
execute if entity @a[tag=lk.N0013] store result score #hoppers lk.hoppers run scoreboard players get @a[tag=lk.N0013,limit=1] lk.hoppers

execute unless entity @a[tag=lk.N0014] unless score #levels lk.levels matches ..0 run scoreboard players remove #levels lk.levels 1
execute if entity @a[tag=lk.N0014] store result score #levels lk.levels run scoreboard players get @a[tag=lk.N0014,limit=1] lk.levels

schedule function lockout:tick/10t 10t replace