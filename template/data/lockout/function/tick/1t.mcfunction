execute as @a[scores={lk.fall=300..,lk.fall_dmg=1..}] run function lockout:goals/n0014
execute as @a[scores={lk.logoff=1..}] if score #game_begun lk.util matches 1 run function lockout:game/resume

scoreboard players set @a lk.fall 0
scoreboard players set @a lk.fall_dmg 0
