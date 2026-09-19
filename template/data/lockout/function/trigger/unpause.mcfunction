execute if score #paused lk.util matches 0 run return fail

execute as @a run function lockout:game/unpause
tick unfreeze

scoreboard players set #paused lk.util 0
