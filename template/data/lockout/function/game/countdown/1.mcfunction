execute as @a at @s run playsound block.note_block.bass master @s ~ ~ ~ 1 1
title @a title {"text": "1", "color": "red"}
tellraw @a {"text": "Game starts in 1..", "color": "red"}
schedule function lockout:game/set_state/game 1s replace
