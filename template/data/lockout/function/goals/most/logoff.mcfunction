scoreboard players remove @s lk.points 1

execute at @a run playsound minecraft:block.beacon.deactivate master @a ~ ~ ~

$say The point for most $(type) was removed due to the player disconnecting.

$tag @s remove lk.$(goalid)