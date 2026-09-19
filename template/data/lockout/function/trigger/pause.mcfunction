execute if score #paused lk.util matches 1 run return fail

execute as @a run function lockout:game/pause
tick freeze

scoreboard players set #paused lk.util 1
