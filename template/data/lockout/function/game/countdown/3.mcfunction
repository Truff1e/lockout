execute as @a at @s run playsound block.note_block.bass master @s ~ ~ ~ 1 1
title @a title {"text": "3", "color": "yellow"}
tellraw @a {"text": "Game starts in 3..", "color": "yellow"}
schedule function lockout:game/countdown/2 1s replace
