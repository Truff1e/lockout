scoreboard players add @s lk.unique_foods 1
execute if score @s lk.unique_foods matches 10.. as @s run function lockout:goals/e0008
execute if score @s lk.unique_foods matches 20.. as @s run function lockout:goals/e0009
execute if score #show_progress lk.util matches 1 if predicate lockout:unique/foods run title @s actionbar [{"text": "You have eaten ", "italic": true, "color": "gray"},{"score":{"name": "@s", "objective": "lk.unique_foods"}, "italic": true, "color": "gray"},{"text": " unique foods", "italic": true, "color": "gray"}]