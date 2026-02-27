execute if score #end_seen lk.util matches 1 run return fail

execute if score #end_on_win lk.util matches 1 as @e[type=armor_stand,tag=lk.team1pts] if score @s lk.points >= #boardSize lk.util unless score #end_seen lk.util matches 1 run function lockout:game/end/win
execute if score #end_on_win lk.util matches 1 as @e[type=armor_stand,tag=lk.team2pts] if score @s lk.points >= #boardSize lk.util unless score #end_seen lk.util matches 1 run function lockout:game/end/win
execute if score #allow_resign lk.util matches 1 as @r[scores={resign=1..}, team=1] unless entity @a[scores={resign=0}, team=1] run function lockout:game/end/resign
execute if score #allow_resign lk.util matches 1 as @r[scores={resign=1..}, team=2] unless entity @a[scores={resign=0}, team=2] run function lockout:game/end/resign
execute if score #allow_draw lk.util matches 1 as @r[scores={draw=1..}] unless entity @a[scores={draw=0}, predicate=lockout:is_playing] run function lockout:game/end/draw
