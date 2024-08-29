say wins!
gamemode spectator @a
tellraw @a [{"text": "Team 1 Score: "},{"score": {"name": "@r[team=1]", "objective": "lk.points"}}]
tellraw @a [{"text": "Team 2 Score: "},{"score": {"name": "@r[team=2]", "objective": "lk.points"}}]
tellraw @a [{"text": "Game Time: "},{"score": {"name": "#game_time", "objective": "lk.util"}},{"text": "min"}]
execute as @a run tellraw @a [{"selector": "@s"},{"text": " completed "}, {"score": {"name": "@s", "objective": "lk.stat.points"}}, {"text": " goals."}]
execute as @a run tellraw @a [{"selector": "@s"},{"text": " failed "}, {"score": {"name": "@s", "objective": "lk.stat.failed_goals"}}, {"text": " goals."}]
execute as @a run tellraw @a [{"selector": "@s"},{"text": " died "}, {"score": {"name": "@s", "objective": "lk.stat.deaths"}}, {"text": " times."}]
execute as @a run tellraw @a [{"selector": "@s"},{"text": " killed "}, {"score": {"name": "@s", "objective": "lk.stat.kills"}}, {"text": " players."}]
scoreboard players set #end_seen lk.util 1
execute as @a run function lockout:game/dump_stats