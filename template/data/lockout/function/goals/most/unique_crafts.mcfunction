execute as @s[tag=!lk.N0015] unless entity @a[tag=lk.N0015] if score @s lk.unique_crafts matches 1.. run function lockout:goals/n0015
execute as @s[tag=!lk.N0015] if score @s lk.unique_crafts > @p[tag=lk.N0015] lk.unique_crafts run function lockout:goals/n0015