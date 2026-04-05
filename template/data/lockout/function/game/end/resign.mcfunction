say resigned.
gamemode spectator @a

function lockout:game/end/message {"end_reason": "Resign"}

scoreboard players set @a resign 0
