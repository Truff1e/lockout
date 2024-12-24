tellraw @a {"text": "---------------------------------","color": "gray"}
tellraw @a [{"selector": "@s"},{"text": " completed "}, {"score": {"name": "@s", "objective": "lk.points"}}, {"text": " goals."}]
tellraw @a [{"selector": "@s"},{"text": " failed "}, {"score": {"name": "@s", "objective": "lk.stat.failed_goals"}}, {"text": " goals."}]
tellraw @a [{"selector": "@s"},{"text": " died "}, {"score": {"name": "@s", "objective": "lk.stat.deaths"}}, {"text": " times."}]
tellraw @a [{"selector": "@s"},{"text": " killed "}, {"score": {"name": "@s", "objective": "lk.stat.kills"}}, {"text": " players."}]