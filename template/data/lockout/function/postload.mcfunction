#team scorebaord entities
forceload add 0 0
execute unless entity @e[type=armor_stand,tag=lk.goaltracker] run summon minecraft:armor_stand 0 319 0 {NoGravity:1b,Marker:1b,Invisible:1b,Tags:["lk.goaltracker"]}
execute unless entity @e[type=armor_stand,tag=lk.team1pts] run summon minecraft:armor_stand 0 319 0 {NoGravity:1b,Marker:1b,Invisible:1b,Tags:["lk.team1pts"],CustomName:'"Team 1"'}
execute unless entity @e[type=armor_stand,tag=lk.team2pts] run summon minecraft:armor_stand 0 319 0 {NoGravity:1b,Marker:1b,Invisible:1b,Tags:["lk.team2pts"],CustomName:'"Team 2"'}

team join 1 @e[tag=lk.team1pts]
team join 2 @e[tag=lk.team2pts]

function lockout:splash
