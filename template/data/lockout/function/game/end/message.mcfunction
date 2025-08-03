tellraw @a {"text": "========================================", "color": "gray"}
$tellraw @a {"text": "Game Over - $(end_reason)", "bold": true, "color": "yellow"}
tellraw @a {"text": "----------------------------------------", "color": "gray"}
tellraw @a [{"text": "Team 1 Score: ", "color":"dark_purple"},{"score": {"name": "@e[type=armor_stand,tag=lk.team1pts]", "objective": "lk.points"}}]
tellraw @a [{"text": "Team 2 Score: ", "color":"dark_aqua"},{"score": {"name": "@e[type=armor_stand,tag=lk.team2pts]", "objective": "lk.points"}}]
tellraw @a [{"text": "Game Length: ", "color":"gold"},{"score": {"name": "#game_time", "objective": "lk.util"}},{"text": "min"}]
tellraw @a {"text": "\n"}
tellraw @a {"text": "Player Stats", "bold": true, "color": "light_purple"}
tellraw @a {"text": "----------------------------------------", "color": "gray"}

execute as @a run function lockout:game/stats/global
scoreboard players set #end_seen lk.util 1
tellraw @a {"text": "========================================", "color": "gray"}
#execute as @a run function lockout:game/stats/personal #disabled because you can see this info in global stats
