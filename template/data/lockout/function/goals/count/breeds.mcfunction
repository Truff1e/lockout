scoreboard players add @s lk.unique_breeds 1

execute if score @s lk.unique_breeds matches 4.. as @s run function lockout:goals/b0018
execute if score @s lk.unique_breeds matches 6.. as @s run function lockout:goals/b0019
execute if score @s lk.unique_breeds matches 8.. as @s run function lockout:goals/b0020
execute if score @s lk.unique_breeds matches 12.. as @s run function lockout:goals/b0021

execute if score #show_progress lk.util matches 1 if predicate lockout:unique/breeds run title @s actionbar [{"text": "You have bred ", "italic": true, "color": "gray"},{"score":{"name": "@s", "objective": "lk.unique_breeds"}, "italic": true, "color": "gray"},{"text": " unique mobs", "italic": true, "color": "gray"}]
