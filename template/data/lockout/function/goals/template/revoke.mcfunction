$execute unless score #$(goalid) lk.enabled_goals matches 1 run return fail
execute if score #state lk.util matches 3 run return fail
$execute unless entity @e[tag=lk.$(goalid)] run return fail
$execute unless entity @s[tag=lk.$(goalid)] run return fail
execute if entity @s[predicate=!lockout:is_playing] run return fail

$tag @s remove lk.$(goalid)
$tag @e[tag=lk.goaltracker] remove lk.$(goalid)
$scoreboard players set @s lk.goal $(goalnum)
execute as @s run function lockout:game/revokegoal
scoreboard players remove @s lk.points 1
execute as @s[team=1] run scoreboard players remove @e[tag=lk.team1pts] lk.points 1
execute as @s[team=2] run scoreboard players remove @e[tag=lk.team2pts] lk.points 1
$say "$(goalname)" was revoked by an operator
