data merge entity @s[type=creeper] {Fuse:20,ExplosionRadius:10,active_effects:[{id:"minecraft:speed",amplifier:2,duration:100000}]}
item replace entity @s[type=zombie] weapon.mainhand with diamond_sword
item replace entity @s[type=zombie] armor.chest with diamond_chestplate
item replace entity @s[type=zombie] armor.feet with diamond_boots
data merge entity @s[type=zombie] {drop_chances:{mainhand:0}}

item replace entity @s[type=#minecraft:skeletons] weapon.mainhand with bow[enchantments={power:3}]

tag @s add lk.initialized
