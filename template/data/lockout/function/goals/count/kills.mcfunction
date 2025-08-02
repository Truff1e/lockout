scoreboard players add @s lk.unique_mobs 1

execute if score @s lk.unique_mobs matches 7.. as @s run function lockout:goals/k0037
execute if score @s lk.unique_mobs matches 15.. as @s run function lockout:goals/k0038

execute if score #show_progress lk.util matches 1 if predicate lockout:unique/kills run title @s actionbar [{"text": "You have killed ", "italic": true, "color": "gray"},{"score":{"name": "@s", "objective": "lk.unique_mobs"}, "italic": true, "color": "gray"},{"text": " unique mobs", "italic": true, "color": "gray"}]
