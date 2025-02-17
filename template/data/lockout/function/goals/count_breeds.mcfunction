scoreboard players add @s lk.unique_breeds 1
execute if score @s lk.unique_breeds matches 6.. as @s run function lockout:goals/b0013
execute if score @s lk.unique_breeds matches 8.. as @s run function lockout:goals/b0014
execute if score @s lk.unique_breeds matches 12.. as @s run function lockout:goals/b0023
execute if score @s lk.unique_breeds matches 15.. as @s run function lockout:goals/b0024
execute if score #show_progress lk.util matches 1 run title @s actionbar [{"text": "You have bred ", "italic": true, "color": "gray"},{"score":{"name": "@s", "objective": "lk.unique_breeds"}, "italic": true, "color": "gray"},{"text": " unique mobs", "italic": true, "color": "gray"}]