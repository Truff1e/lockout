execute as @e[type=armor_stand,tag=lk.team1pts] if score @s lk.points >= #boardSize lk.util unless score #end_seen lk.util matches 1 run function lockout:game/win
execute as @e[type=armor_stand,tag=lk.team2pts] if score @s lk.points >= #boardSize lk.util unless score #end_seen lk.util matches 1 run function lockout:game/win
execute as @r[scores={resign=1..}, team=1] unless entity @a[scores={resign=0}, team=1] run function lockout:game/resign
execute as @r[scores={resign=1..}, team=2] unless entity @a[scores={resign=0}, team=2] run function lockout:game/resign
execute as @r[scores={draw=1..}] unless entity @a[scores={draw=0}, team=!spectator] run function lockout:game/draw