tellraw @a {"text": "---------------------------------","color": "gray"}
tellraw @a [{"selector": "@s"},{"text": " completed "}, {"score": {"name": "@s", "objective": "lk.points"}}, {"text": " goals."}]
tellraw @a [{"selector": "@s"},{"text": " failed "}, {"score": {"name": "@s", "objective": "lk.stat.failed_goals"}}, {"text": " goals."}]
tellraw @a [{"selector": "@s"},{"text": " died "}, {"score": {"name": "@s", "objective": "lk.stat.deaths"}}, {"text": " times."}]
tellraw @a [{"selector": "@s"},{"text": " killed "}, {"score": {"name": "@s", "objective": "lk.stat.kills"}}, {"text": " players."}]
tellraw @a {"text": "----------------","color": "gray"}
tellraw @a [{"selector": "@s","bold":true,"color":"light_purple"},{"text":"'s Goal Progress","bold":true,"color":"light_purple"}]
tellraw @a [{"text":"Unique Advancements: "},{"score":{"name":"@s","objective":"lk.unique_advancements"}}]
tellraw @a [{"text":"Unique Breeds: "},{"score":{"name":"@s","objective":"lk.unique_breeds"}}]
tellraw @a [{"text":"Unique Crafts: "},{"score":{"name":"@s","objective":"lk.unique_crafts"}}]
tellraw @a [{"text":"Unique Foods: "},{"score":{"name":"@s","objective":"lk.unique_foods"}}]
tellraw @a [{"text":"Unique Hostile Mobs: "},{"score":{"name":"@s","objective":"lk.unique_mobs"}}]
tellraw @a [{"text":"Levels: "},{"score":{"name":"@s","objective":"lk.levels"}}]
