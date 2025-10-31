execute if score #show_progress lk.util matches 0 run return fail 

tellraw @s ["",{"text":"======================","color":"gray"},{"text":"\n"},{"text":"Goal Progress","bold":true,"color":"light_purple"},{"text":"\n\nUnique Advancements: "},{"score":{"name":"@s","objective":"lk.unique_advancements"}},{"text":"\nUnique Breeds: "},{"score":{"name":"@s","objective":"lk.unique_breeds"}},{"text":"\nUnique Crafts: "},{"score":{"name":"@s","objective":"lk.unique_crafts"}},{"text":"\nUnique Foods: "},{"score":{"name":"@s","objective":"lk.unique_foods"}},{"text":"\nUnique Hostile Mobs: "},{"score":{"name":"@s","objective":"lk.unique_mobs"}},{"text":"\n"},{"text":"======================","color":"gray"}]

scoreboard players set @s progress 0
