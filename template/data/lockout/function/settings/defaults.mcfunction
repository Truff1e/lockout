#if the game has already been initialized, don't reset the scores
execute if score #initialized lk.util matches 1 run return fail
#settings
scoreboard players set #start_time lk.util 45
scoreboard players set #max_time lk.util 120
scoreboard players set #show_progress lk.util 1
scoreboard players set #allow_pvp lk.util 1
scoreboard players set #allow_locator lk.util 1
scoreboard players set #allow_draw lk.util 1
scoreboard players set #allow_resign lk.util 1
scoreboard players set #end_on_win lk.util 1
scoreboard players set #friendly_fire lk.util 1

scoreboard players set #show_timer lk.util 1
