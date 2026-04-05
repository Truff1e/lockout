execute as @a at @s run playsound block.note_block.bass master @s ~ ~ ~ 1 1
title @a title {"text": "2", "color": "gold"}
tellraw @a {"text": "Game starts in 2..", "color": "gold"}
schedule function lockout:game/countdown/1 1s replace
