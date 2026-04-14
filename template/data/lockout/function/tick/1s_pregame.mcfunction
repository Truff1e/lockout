scoreboard players remove #timer_pregame lk.util 1
function lockout:timer/pregame

gamemode spectator @a[team=spectator]

execute unless score #state lk.util matches 2.. run schedule function lockout:tick/1s_pregame 1s
