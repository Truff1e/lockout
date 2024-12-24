execute if score @s[tag=!lk.N0012] lk.dried_kelp > #dried_kelp lk.util run function lockout:goals/n0012

execute as @s[tag=lk.N0012] if score @s lk.dried_kelp >= #dried_kelp lk.util store result score #dried_kelp lk.util run scoreboard players get @s lk.dried_kelp

execute as @s[tag=lk.N0012] unless score @s lk.dried_kelp >= #dried_kelp lk.util run tag @s remove lk.N0012
execute unless entity @a[tag=lk.N0012] if score #dried_kelp lk.util matches 0.. run scoreboard players remove #dried_kelp lk.util 1
execute unless entity @a[tag=lk.N0012] if score #dried_kelp lk.util matches 1.. run schedule function lockout:goals/dried_kelp 1t