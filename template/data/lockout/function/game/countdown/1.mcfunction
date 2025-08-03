title @a title {"text": "1", "color": "red"}
tellraw @a {"text": "Game starts in 1..", "color": "red"}
schedule function lockout:game/countdown/go 1s replace
