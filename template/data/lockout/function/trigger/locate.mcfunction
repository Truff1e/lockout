execute if score #allow_locator lk.util matches 0 run return fail

execute as @a run function lockout:update_location

execute as @a[team=!spectator] run tellraw @a[scores={locate=1..}] [{"selector": "@s"},{"text": " is at "},{"score":{"name": "@s", "objective": "lk.posX"}},{"text": ", "},{"score":{"name": "@s", "objective": "lk.posZ"}},{"text": " in the "},{"nbt":"Dimension","entity":"@s"}]


scoreboard players set @a locate 0
