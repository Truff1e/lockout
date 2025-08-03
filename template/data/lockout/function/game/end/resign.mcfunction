say resigned.
execute at @a run playsound entity.ender_dragon.death master @a ~ ~ ~
gamemode spectator @a

function lockout:game/end/message {"end_reason": "Resign"}

scoreboard players set @a resign 0
