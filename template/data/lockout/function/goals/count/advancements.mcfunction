scoreboard players add @s lk.unique_advancements 1

execute if score @s lk.unique_advancements matches 25.. as @s run function lockout:goals/a0001
execute if score @s lk.unique_advancements matches 15.. as @s run function lockout:goals/a0021
execute if score @s lk.unique_advancements matches 35.. as @s run function lockout:goals/a0022
execute if score #show_progress lk.util matches 1 if predicate lockout:unique/advancements run title @s actionbar [{"text": "You have gotten ", "italic": true, "color": "gray"},{"score":{"name": "@s", "objective": "lk.unique_advancements"}, "italic": true, "color": "gray"},{"text": " unique advancements", "italic": true, "color": "gray"}]