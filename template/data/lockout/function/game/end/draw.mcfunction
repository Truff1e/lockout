gamemode spectator @a

function lockout:game/end/message {"end_reason": "Draw"}

scoreboard players set @a draw 0
