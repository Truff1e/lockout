tellraw @a {"text": "The game time limit has expired.", "color": "dark_red"}
gamemode spectator @a
execute as @a run function lockout:game/stats/personal
tellraw @a [{"text": "Team 1 Score: "},{"score": {"name": "@r[team=1]", "objective": "lk.points"}}]
tellraw @a [{"text": "Team 2 Score: "},{"score": {"name": "@r[team=2]", "objective": "lk.points"}}]
tellraw @a [{"text": "Game Time: "},{"score": {"name": "#game_time", "objective": "lk.util"}},{"text": "m"}]
execute as @a run function lockout:game/stats/global
scoreboard players set #end_seen lk.util 1