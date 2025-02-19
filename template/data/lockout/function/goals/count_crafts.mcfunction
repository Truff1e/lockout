scoreboard players add @s lk.unique_crafts 1
execute if score #N0015 lk.enabled_goals matches 1 as @s run function lockout:goals/most/unique_crafts
execute as @s[scores={lk.unique_crafts=25}] run function lockout:goals/x0036
execute as @s[scores={lk.unique_crafts=50}] run function lockout:goals/x0037
execute as @s[scores={lk.unique_crafts=75}] run function lockout:goals/x0038
execute if score #show_progress lk.util matches 1 if predicate lockout:unique/crafts run title @s actionbar [{"text": "You have crafted ", "italic": true, "color": "gray"},{"score":{"name": "@s", "objective": "lk.unique_crafts"}, "italic": true, "color": "gray"},{"text": " unique items", "italic": true, "color": "gray"}]