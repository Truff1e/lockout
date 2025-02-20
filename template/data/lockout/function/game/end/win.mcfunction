say wins!
execute at @a run playsound entity.ender_dragon.death master @a ~ ~ ~
gamemode spectator @a
tellraw @a [{"text": "Team 1 Score: "},{"score": {"name": "@e[type=armor_stand,tag=lk.team1pts]", "objective": "lk.points"}}]
tellraw @a [{"text": "Team 2 Score: "},{"score": {"name": "@e[type=armor_stand,tag=lk.team2pts]", "objective": "lk.points"}}]
tellraw @a [{"text": "Game Time: "},{"score": {"name": "#game_time", "objective": "lk.util"}},{"text": "min"}]
execute as @a run function lockout:game/stats/global
scoreboard players set #end_seen lk.util 1
execute as @a run function lockout:game/stats/personal