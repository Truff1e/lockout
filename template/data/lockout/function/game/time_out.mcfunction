tellraw @a {"text": "The game time limit has expired.", "color": "dark_red"}
gamemode spectator @a
execute as @a run function lockout:game/dump_stats
tellraw @a [{"text": "Team 1 Score: "},{"score": {"name": "@r[team=1]", "objective": "lk.points"}}]
tellraw @a [{"text": "Team 2 Score: "},{"score": {"name": "@r[team=2]", "objective": "lk.points"}}]
tellraw @a [{"text": "Game Time: "},{"score": {"name": "#game_time", "objective": "lk.util"}},{"text": "m"}]
execute as @a run function lockout:game/print_stats
scoreboard players set #end_seen lk.util 1