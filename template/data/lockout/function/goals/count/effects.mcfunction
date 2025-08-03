scoreboard players add @s[predicate=lockout:effects/absorption] lk.unique_effects 1
scoreboard players add @s[predicate=lockout:effects/bad_omen] lk.unique_effects 1
scoreboard players add @s[predicate=lockout:effects/blindness] lk.unique_effects 1
scoreboard players add @s[predicate=lockout:effects/conduit_power] lk.unique_effects 1
scoreboard players add @s[predicate=lockout:effects/darkness] lk.unique_effects 1
scoreboard players add @s[predicate=lockout:effects/dolphins_grace] lk.unique_effects 1
scoreboard players add @s[predicate=lockout:effects/fire_resistance] lk.unique_effects 1
scoreboard players add @s[predicate=lockout:effects/glowing] lk.unique_effects 1
scoreboard players add @s[predicate=lockout:effects/haste] lk.unique_effects 1
scoreboard players add @s[predicate=lockout:effects/health_boost] lk.unique_effects 1
scoreboard players add @s[predicate=lockout:effects/hero_of_the_village] lk.unique_effects 1
scoreboard players add @s[predicate=lockout:effects/hunger] lk.unique_effects 1
scoreboard players add @s[predicate=lockout:effects/infested] lk.unique_effects 1
scoreboard players add @s[predicate=lockout:effects/invisibility] lk.unique_effects 1
scoreboard players add @s[predicate=lockout:effects/jump_boost] lk.unique_effects 1
scoreboard players add @s[predicate=lockout:effects/levitation] lk.unique_effects 1
scoreboard players add @s[predicate=lockout:effects/luck] lk.unique_effects 1
scoreboard players add @s[predicate=lockout:effects/mining_fatigue] lk.unique_effects 1
scoreboard players add @s[predicate=lockout:effects/nausea] lk.unique_effects 1
scoreboard players add @s[predicate=lockout:effects/night_vision] lk.unique_effects 1
scoreboard players add @s[predicate=lockout:effects/oozing] lk.unique_effects 1
scoreboard players add @s[predicate=lockout:effects/poison] lk.unique_effects 1
scoreboard players add @s[predicate=lockout:effects/raid_omen] lk.unique_effects 1
scoreboard players add @s[predicate=lockout:effects/regeneration] lk.unique_effects 1
scoreboard players add @s[predicate=lockout:effects/resistance] lk.unique_effects 1
scoreboard players add @s[predicate=lockout:effects/saturation] lk.unique_effects 1
scoreboard players add @s[predicate=lockout:effects/slow_falling] lk.unique_effects 1
scoreboard players add @s[predicate=lockout:effects/slowness] lk.unique_effects 1
scoreboard players add @s[predicate=lockout:effects/speed] lk.unique_effects 1
scoreboard players add @s[predicate=lockout:effects/strength] lk.unique_effects 1
scoreboard players add @s[predicate=lockout:effects/trial_omen] lk.unique_effects 1
scoreboard players add @s[predicate=lockout:effects/unluck] lk.unique_effects 1
scoreboard players add @s[predicate=lockout:effects/water_breathing] lk.unique_effects 1
scoreboard players add @s[predicate=lockout:effects/weakness] lk.unique_effects 1
scoreboard players add @s[predicate=lockout:effects/wind_charged] lk.unique_effects 1
scoreboard players add @s[predicate=lockout:effects/wither] lk.unique_effects 1

execute if score #test_effects lk.util matches 1 as @s[scores={lk.unique_effects=3..}] run function lockout:goals/x0018
execute if score #test_effects lk.util matches 1 as @s[scores={lk.unique_effects=6..}] run function lockout:goals/x0019
execute as @s[scores={lk.unique_effects=9..}] run function lockout:goals/x0020
execute as @s[scores={lk.unique_effects=12..}] run function lockout:goals/x0021

execute if score #show_progress lk.util matches 1 if predicate lockout:unique/effects run title @s actionbar [{"text": "You have ", "italic": true, "color": "gray"},{"score":{"name": "@s", "objective": "lk.unique_effects"}, "italic": true, "color": "gray"},{"text": " unique effects", "italic": true, "color": "gray"}]

scoreboard players set @s lk.unique_effects 0
advancement revoke @s only lockout:goals/unique_effects/unique_effects
