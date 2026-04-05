$effect give @a minecraft:mining_fatigue $(time) 9 true
$effect give @a minecraft:weakness $(time) 9 true
$effect give @a minecraft:resistance $(time) 4 true
$schedule function lockout:game/countdown/3 $(time)s replace
$scoreboard players set #timer_pregame lk.util $(time)
scoreboard players add #timer_pregame lk.util 3
