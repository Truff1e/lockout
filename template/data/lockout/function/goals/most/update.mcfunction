## Update "Most" Goal
## Takes 4 parameters: id, name, readable_name, minimum

# Detect when a player with the most of something logs off
$execute unless entity @a[tag=lk.M$(id)] as @e[type=armor_stand,tag=lk.M$(id),tag=!lk.goaltracker] run function lockout:goals/most/logoff {"id": "M$(id)", "type": "$(readable_name)"}

# Check if a player is now the new highest player
$execute if score #M$(id) lk.enabled_goals matches 1 as @a[predicate=lockout:most/$(name),limit=1,sort=random,tag=!lk.M$(id)] if score @s lk.$(name) > #$(name) lk.most run function lockout:goals/m$(id)

# Decrement the placeholder value until the next highest player found
$execute unless entity @a[tag=lk.M$(id)] unless score #$(name) lk.most matches ..$(minimum) run scoreboard players remove #$(name) lk.most 1

# Store the current highest value in placeholder
$execute if entity @a[tag=lk.M$(id)] store result score #$(name) lk.most run scoreboard players get @a[tag=lk.M$(id),limit=1] lk.$(name)
