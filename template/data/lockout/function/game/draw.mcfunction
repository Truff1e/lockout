tellraw @s {"text": "The game ended in a draw."}
execute at @a run playsound entity.ender_dragon.death master @a ~ ~ ~
gamemode spectator @a
tellraw @a [{"text": "Team 1 Score: "},{"score": {"name": "@r[team=1]", "objective": "lk.points"}}]
tellraw @a [{"text": "Team 2 Score: "},{"score": {"name": "@r[team=2]", "objective": "lk.points"}}]
tellraw @a [{"text": "Game Time: "},{"score": {"name": "#game_time", "objective": "lk.util"}},{"text": "min"}]
execute as @a run function lockout:game/print_stats
scoreboard players set #end_seen lk.util 1
execute as @a run function lockout:game/dump_stats


scoreboard players set @a draw 0