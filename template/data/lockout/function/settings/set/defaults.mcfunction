execute if score #friendly_fire lk.util matches 1 run function lockout:settings/set/enable_friendly_fire
execute if score #friendly_fire lk.util matches 0 run function lockout:settings/set/disable_friendly_fire
execute if score #allow_pvp lk.util matches 1 run gamerule pvp true
execute if score #allow_pvp lk.util matches 0 run gamerule pvp false
function lockout:settings/set/max_time
function lockout:settings/set/start_time
