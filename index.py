import random
import json
import os


def parse_options():
    # Reads data stored in options.txt and translates it to a settings list
    optionsfile = open(os.path.join(os.path.dirname(__file__), 'options.txt'), 'r')
    optionslist = {}
    for line in optionsfile:
        optionslist[line[:line.find('=')]] = line[line.find('=')+1:-1]
    return optionslist


goalIndex = {
        # id: [name, icon, customModelDataBool, difficulty, description]
        # Commented out goals are not yet implemented or are broken

        # KILL GOALS
        'K0001': ['Kill Bat', 'iron_sword', True, 1],
        'K0002': ['Kill Bee', 'iron_sword', True, 2],
        'K0003': ['Kill Blaze', 'iron_sword', True, 4],
        'K0004': ['Kill Cave Spider', 'iron_sword', True, 4],
        'K0005': ['Kill Drowned', 'iron_sword', True, 2],
        'K0006': ['Kill Elder Guardian', 'iron_sword', True, 4],
        'K0007': ['Kill Ender Dragon', 'dragon_head', True, 8],
        'K0008': ['Kill Endermite', 'iron_sword', True, 6],
        'K0009': ['Kill Evoker', 'iron_sword', True, 7],
        'K0010': ['Kill Ghast', 'iron_sword', True, 3],
        'K0011': ['Kill Guardian', 'iron_sword', True, 4],
        'K0012': ['Kill Husk', 'iron_sword', True, 4],
        'K0013': ['Kill Magma Cube', 'iron_sword', True, 2],
        'K0014': ['Kill Piglin Brute', 'iron_sword', True, 5],
        'K0015': ['Kill Pillager', 'iron_sword', True, 4],
        'K0016': ['Kill Player', 'diamond_sword', True, 3],
        'K0017': ['Kill Ravager', 'iron_sword', True, 6],
        'K0018': ['Kill Shulker', 'iron_sword', True, 9],
        'K0019': ['Kill Silverfish', 'iron_sword', True, 5],
        'K0020': ['Kill Slime', 'iron_sword', True, 4],
        'K0021': ['Kill Snow Golem', 'iron_sword', True, 3],
        'K0022': ['Kill Spider', 'iron_sword', True, 1],
        'K0023': ['Kill Stray', 'iron_sword', True, 4],
        'K0024': ['Kill Vex', 'iron_sword', True, 7],
        'K0025': ['Kill Witch', 'iron_sword', True, 4],
        'K0026': ['Kill Wither Skeleton', 'iron_sword', True, 4],
        'K0027': ['Kill Zoglin', 'iron_sword', True, 5],
        'K0028': ['Kill Zombie Villager', 'iron_sword', True, 4],
        'K0029': ['Kill Zombie', 'iron_sword', True, 1],
        'K0030': ['Kill Zombified Piglin', 'iron_sword', True, 2],
        'K0031': ['Kill 30 Mobs', 'iron_sword', True, 1],
        'K0032': ['Kill 100 Mobs', 'iron_sword', True, 2],
        # 'K0033': ['Kill 30 Undead Mobs', 'iron_sword', True, 2],
        # 'K0034': ['Kill 30 Arthropods', 'iron_sword', True, 2],
        # 'K0035': ['Kill 10 Ghasts', 'iron_sword', True, 3],
        # 'K0036': ['Kill 10 Endermen', 'iron_sword', True, 3],
        'K0037': ['Kill 7 Unique Hostile Mobs', 'iron_sword', True, 3],
        'K0038': ['Kill 15 Unique Hostile Mobs', 'iron_sword', True, 5],
        # 'K0039': ['Kill Every Undead Mob', 'iron_sword', True, 5],

        # DEATH GOALS
        'D0001': ['Die to Bee', 'beehive', True, 1],
        'D0002': ['Die to Llama', 'hay_block', True, 3],
        'D0003': ['Die to Iron Golem', 'carved_pumpkin', True, 2],
        'D0004': ['Die to Witch', 'glass_bottle', True, 2],
        'D0005': ['Die to Piglin Brute', 'golden_axe', True, 3],
        'D0006': ['Die on Pointed Dripstone', 'pointed_dripstone', True, 2],
        'D0007': ['Die to Polar Bear', 'cod', True, 3],

        # HAVE MORE GOALS
        'M0012': ['Have the Most Dried Kelp Blocks', 'dried_kelp_block', True, 3],
        'M0013': ['Have the Most Hoppers', 'hopper', True, 3],
        'M0014': ['Have the Most Levels', 'experience_bottle', True, 3],
        'M0015': ['Have the Most Unique Crafts', 'crafting_table', True, 3],

        # HUSBANDRY GOALS
        'T0001': ['Tame Cat', 'cod', True, 2],
        'T0002': ['Tame Wolf', 'bone', True, 2],
        'T0003': ['Tame Horse', 'golden_carrot', True, 2],
        'T0004': ['Tame Donkey', 'golden_carrot', True, 3],
        'T0005': ['Tame Mule', 'golden_carrot', True, 5],
        'T0006': ['Tame Parrot', 'melon_seeds', True, 4],
        'T0007': ['Tame Llama', 'hay_block', True, 4],
        # 'T0008': ['Tame 5 Cat Variants', 'cod', True, 5],
        'T0009': ['Tame Every Cat Variant', 'cod', True, 9],

        # BREEDING GOALS
        'B0001': ['Breed Axolotl', 'tropical_fish_bucket', True, 4],
        'B0002': ['Breed Cat', 'cod', True, 3],
        'B0003': ['Breed Chicken', 'wheat_seeds', True, 1],
        'B0004': ['Breed Cow', 'wheat', True, 2],
        'B0005': ['Breed Fox', 'sweet_berries', True, 4],
        'B0006': ['Breed Goat', 'wheat', True, 3],
        'B0007': ['Breed Hoglin', 'crimson_fungus', True, 3],
        'B0008': ['Breed Horse', 'golden_carrot', True, 2],
        'B0009': ['Breed Mooshroom', 'red_mushroom', True, 6],
        'B0010': ['Breed Ocelot', 'cod', True, 6],
        'B0011': ['Breed Panda', 'bamboo', True, 5],
        'B0012': ['Breed Pig', 'potato', True, 2],
        'B0013': ['Breed Rabbit', 'carrot', True, 3],
        'B0014': ['Breed Sheep', 'wheat', True, 1],
        'B0015': ['Breed Strider', 'warped_fungus', True, 3],
        'B0016': ['Breed Turtle', 'seagrass', True, 3],
        'B0017': ['Breed Wolf', 'bone', True, 3],
        'B0018': ['Breed 4 Unique Mobs', 'wheat', True, 2],
        'B0019': ['Breed 6 Unique Mobs', 'wheat', True, 3],
        'B0020': ['Breed 8 Unique Mobs', 'wheat', True, 4],
        'B0021': ['Breed 12 Unique Mobs', 'wheat', True, 7],

        # ITEM GOALS
        'I0001': ['Obtain All Swords', 'netherite_sword', True, 6], #TODO: Add Copper 
        'I0002': ['Obtain All Axes', 'netherite_axe', True, 6], #TODO: Add Copper 
        'I0003': ['Obtain All Pickaxes', 'netherite_pickaxe', True, 6], #TODO: Add Copper 
        'I0004': ['Obtain All Shovels', 'netherite_shovel', True, 6], #TODO: Add Copper 
        'I0005': ['Obtain All Hoes', 'netherite_hoe', True, 6], #TODO: Add Copper 
        'I0006': ['Obtain Full Leather Armor', 'leather_chestplate', True, 2],
        'I0007': ['Obtain Chainmail Armor', 'chainmail_helmet', False, 4],
        'I0008': ['Obtain Full Chainmail Armor', 'chainmail_chestplate', True, 7],
        'I0009': ['Obtain Full Iron Armor', 'iron_chestplate', True, 3],
        'I0010': ['Obtain Full Gold Armor', 'golden_chestplate', True, 2],
        'I0011': ['Obtain Diamond Armor', 'diamond_helmet', False, 3],
        'I0012': ['Obtain Full Diamond Armor', 'diamond_chestplate', True, 4],
        'I0013': ['Obtain Netherite Armor', 'netherite_helmet', False, 6],
        'I0014': ['Obtain Full Netherite Armor', 'netherite_chestplate', True, 10],
        'I0015': ['Obtain All Wooden Tools', 'wooden_pickaxe', True, 1],
        'I0016': ['Obtain All Stone Tools', 'stone_pickaxe', True, 1],
        'I0017': ['Obtain All Iron Tools', 'iron_pickaxe', True, 2],
        'I0018': ['Obtain All Gold Tools', 'golden_pickaxe', True, 2],
        'I0019': ['Obtain All Diamond Tools', 'diamond_pickaxe', True, 4],
        'I0020': ['Obtain All Netherite Tools', 'netherite_pickaxe', True, 10],
        'I0021': ['Obtain All Log Types', 'jungle_log', True, 8],
        'I0022': ['Obtain All Wool Blocks', 'white_wool', True, 5],
        'I0023': ['Obtain All Rail Types', 'powered_rail', True, 3],
        'I0024': ['Obtain All Raw Ore Blocks', 'raw_iron_block', True, 2],
        'I0025': ['Obtain All Overworld Ores', 'diamond_ore', True, 8],
        'I0026': ['Obtain All Overworld Ore Blocks', 'diamond_block', True, 8],
        'I0027': ['Obtain All Nether Ores', 'nether_gold_ore', True, 6],
        'I0028': ['Obtain All Banner Patterns', 'creeper_banner_pattern', False, 10],
        'I0029': ['Obtain All Nether Ore Blocks', 'netherite_block', True, 10],
        'I0030': ['Obtain Every Horse Armor', 'diamond_horse_armor', True, 6],
        'I0031': ['Obtain Every Type of Seed', 'wheat_seeds', True, 3],
        'I0032': ['Obtain All Minecart Types', 'minecart', True, 3],
        'I0033': ['Obtain All Furnace Variants', 'furnace', False, 1],
        'I0034': ['Obtain All Mushrooms', 'red_mushroom', False, 2],
        'I0035': ['Obtain All Pumpkin Types', 'pumpkin', False, 2],
        'I0036': ['Obtain 5 Unique Saplings', 'oak_sapling', True, 2],
        'I0037': ['Obtain 6 Log Variants', 'acacia_log', False, 3],
        'I0038': ['Obtain 8 Log Variants', 'jungle_log', False, 6],
        'I0039': ['Obtain Cake', 'cake', False, 3],
        'I0040': ['Obtain Cobweb', 'cobweb', False, 3],
        'I0041': ['Obtain Comparator', 'comparator', False, 3],
        'I0042': ['Obtain Repeater', 'repeater', False, 3],
        'I0043': ['Obtain Redstone Lamp', 'redstone_lamp', False, 3],
        'I0044': ['Obtain End Crystal', 'end_crystal', False, 5],
        'I0045': ['Obtain End Rod', 'end_rod', False, 8],
        'I0046': ['Obtain Ender Chest', 'ender_chest', False, 5],
        'I0047': ['Obtain Grass Block', 'grass_block', False, 3],
        'I0048': ['Obtain Honey Bottle', 'honey_bottle', False, 3],
        'I0049': ['Obtain Honey Block', 'honey_block', False, 5],
        'I0050': ['Obtain Mossy Stone Brick Wall', 'mossy_stone_brick_wall', False, 2],
        'I0051': ['Obtain Red Nether Brick Stairs', 'red_nether_brick_stairs', False, 4],
        'I0052': ['Obtain Mushroom Stem', 'mushroom_stem', False, 5],
        'I0053': ['Obtain Powder Snow Bucket', 'powder_snow_bucket', False, 3],
        'I0054': ['Obtain Scaffolding', 'scaffolding', False, 3],
        'I0055': ['Obtain Soul Lantern', 'soul_lantern', False, 3],
        'I0056': ['Obtain Bucket of Tropical Fish', 'tropical_fish_bucket', False, 3],
        'I0057': ['Obtain Wither Skeleton Skull', 'wither_skeleton_skull', False, 5],
        'I0058': ['Obtain Trident', 'trident', False, 7],
        'I0059': ['Obtain Nautilus Shell', 'nautilus_shell', False, 5],
        'I0060': ['Obtain Heart of the Sea', 'heart_of_the_sea', False, 2],
        'I0061': ['Obtain Banner Pattern', 'creeper_banner_pattern', False, 1],
        'I0062': ['Obtain Rabbit Foot', 'rabbit_foot', False, 4],
        'I0063': ['Obtain Totem of Undying', 'totem_of_undying', False, 6],
        'I0064': ['Obtain Name Tag', 'name_tag', False, 4],
        'I0065': ['Obtain Written Book', 'written_book', False, 3],
        'I0066': ['Obtain Bookshelf', 'bookshelf', False, 2],
        'I0067': ['Obtain Sea Lantern', 'sea_lantern', False, 4],
        'I0068': ['Obtain Flowering Azalea', 'flowering_azalea', False, 2],
        'I0069': ['Obtain Bell', 'bell', False, 2],
        'I0070': ['Obtain Ancient Debris', 'ancient_debris', False, 4],
        'I0071': ['Obtain Lodestone', 'lodestone', False, 3],
        'I0072': ['Obtain Sponge', 'sponge', False, 4],
        'I0073': ['Obtain TNT', 'tnt', False, 1],
        'I0074': ['Obtain Goat Horn', 'goat_horn', False, 4],
        'I0075': ['Obtain Daylight Detector', 'daylight_detector', False, 3],
        'I0076': ['Obtain Observer', 'observer', False, 3],
        'I0077': ['Obtain Piston', 'piston', False, 2],
        'I0078': ['Obtain Sticky Piston', 'sticky_piston', False, 5],
        'I0079': ['Obtain Tinted Glass', 'tinted_glass', False, 2],
        'I0080': ['Obtain Sniffer Egg', 'sniffer_egg', False, 5],
        'I0081': ['Obtain Nether Star', 'nether_star', False, 10],
        'I0082': ['Obtain Netherite Ingot', 'netherite_ingot', False, 6],
        'I0083': ['Obtain Glow Item Frame', 'glow_item_frame', False, 2],
        'I0084': ['Obtain Block of Dried Kelp', 'dried_kelp_block', False, 1],
        'I0085': ['Obtain Elytra', 'elytra', False, 9],
        'I0086': ['Obtain Turtle Scute', 'turtle_scute', False, 7],
        'I0087': ['Obtain Glow Lichen', 'glow_lichen', False, 1],
        'I0088': ['Obtain Flower Pot', 'flower_pot', False, 1],
        'I0089': ['Obtain Iron Bars', 'iron_bars', False, 1],
        'I0090': ['Obtain Clock', 'clock', False, 1],
        'I0091': ['Brew Swiftness Potion', 'potion', True, 6],
        'I0092': ['Brew Healing Potion', 'potion', True, 6],
        'I0093': ['Brew Invisibility Potion', 'potion', True, 6],
        'I0094': ['Brew Jump Boost Potion', 'potion', True, 6],
         
        
        'E0001': ['Eat Apple', 'apple', False, 1],
        'E0002': ['Eat Beetroot', 'beetroot', False, 3],
        'E0003': ['Eat Carrot', 'carrot', False, 2],
        'E0004': ['Eat Cookie', 'cookie', False, 3],
        'E0005': ['Eat Dried Kelp', 'dried_kelp', False, 1],
        'E0006': ['Eat Glow Berry', 'glow_berries', False, 2],
        'E0007': ['Eat Poisonous Potato', 'poisonous_potato', False, 2],
        'E0008': ['Eat Pumpkin Pie', 'pumpkin_pie', False, 2],
        'E0009': ['Eat Rabbit Stew', 'rabbit_stew', False, 2],
        'E0010': ['Eat Suspicious Stew', 'suspicious_stew', False, 2],
        'E0011': ['Eat Beetroot Stew', 'beetroot_soup', False, 3],
        'E0012': ['Eat Chorus Fruit', 'chorus_fruit', False, 8],
        'E0013': ['Eat Enchanted Golden Apple', 'enchanted_golden_apple', False, 6],
        'E0014': ['Eat Spider Eye', 'spider_eye', False, 1],
        'E0015': ['Eat 5 Unique Foods', 'apple', True, 1],
        'E0016': ['Eat 10 Unique Foods', 'apple', True, 2],
        'E0017': ['Eat 20 Unique Foods', 'apple', True, 4],


        'A0001': ['Get 15 Unique Advancements', 'experience_bottle', True, 2],
        'A0002': ['Get 25 Unique Advancements', 'experience_bottle', True, 4],
        'A0003': ['Get 35 Unique Advancements', 'experience_bottle', True, 6],
        'A0004': ['Get Bullseye Advancement', 'target', False, 3],
        'A0005': ['Cure Zombie Villager', 'golden_apple', False, 3],
        'A0006': ['Use Enchantment Table', 'enchanting_table', False, 3],
        'A0007': ['Get Oh Shiny Advancement', 'gold_ingot', False, 2],
        'A0008': ['Get Sniper Duel Advancement', 'bow', False, 3],
        'A0009': ['Do any Spyglass Advancement', 'spyglass', False, 2],
        'A0010': ['Do Star Trader Advancement', 'emerald_block', False, 6],
        'A0011': ['Ride Strider', 'warped_fungus_on_a_stick', False, 3],
        'A0012': ['Trade with a Villager', 'emerald', False, 2],
        'A0013': ['Get Subspace Bubble Advancement', 'obsidian', False, 5],
        'A0014': ['Fully Charge Respawn Anchor', 'respawn_anchor', False, 4],
        'A0015': ['Do Power of Books Advancement', 'chiseled_bookshelf', False, 3],
        'A0016': ['Do Caves and Cliffs Advancement', 'water_bucket', False, 6],
        'A0017': ['Summon Iron Golem', 'carved_pumpkin', False, 4],
        'A0018': ['Start a Raid', 'ominous_bottle', False, 6],
        'A0019': ['Locate all Nether Biomes', 'netherite_boots', False, 5],
        'A0020': ['Enter Nether Fortress', 'nether_bricks', False, 3],
        'A0021': ['Enter Bastion', 'gilded_blackstone', False, 3],
        'A0022': ['Enter End City', 'purpur_pillar', False, 9],
        'A0023': ['Enter End', 'end_portal_frame', False, 7],
        'A0024': ['Enter Nether', 'flint_and_steel', True, 2],
        'A0025': ['Locate Stronghold', 'ender_eye', False, 6],


        'X0001': ['Get 5 Levels', 'experience_bottle', True, 1],
        'X0002': ['Get 15 Levels', 'experience_bottle', True, 2],
        'X0003': ['Get 30 Levels', 'experience_bottle', True, 4],
        'X0004': ['Mine Diamond', 'diamond_ore', False, 2],
        'X0005': ['Mine Emerald Ore', 'emerald_ore', False, 3],
        'X0006': ['Mine Mob Spawner', 'spawner', False, 2],
        'X0007': ['Get 64 of the Same Item', 'dirt', True, 1],
        'X0008': ['Sprint 1km', 'diamond_boots', False, 1],
        'X0009': ['Wear a Pumpkin for 5 Minutes', 'carved_pumpkin', False, 2],
        'X0010': ['Take 200 Damage', 'wooden_sword', True, 1],
        'X0011': ['Empty Hunger Bar', 'rotten_flesh', True, 1],
        'X0012': ['Wash Leather Armor', 'cauldron', True, 2],
        'X0013': ['Use a Jukebox', 'jukebox', False, 3],
        'X0014': ['Reach Bedrock', 'bedrock', False, 1],
        'X0015': ['Reach Height Limit', 'glass', True, 1],
        'X0016': ['Travel to Nether Roof', 'bedrock', False, 2],
        'X0017': ['Locate Woodland Mansion', 'red_carpet', False, 4],
        'X0018': ['Have 3 Status Effects at Once', 'milk_bucket', True, 1],
        'X0019': ['Have 6 Status Effects at Once', 'milk_bucket', True, 4],
        'X0020': ['Have 9 Status Effects at Once', 'milk_bucket', True, 6],
        'X0021': ['Have 12 Status Effects at Once', 'milk_bucket', True, 8],
        'X0022': ['Craft 25 Unique Items', 'crafting_table', False, 1],
        'X0023': ['Craft 50 Unique Items', 'crafting_table', False, 2],
        'X0024': ['Craft 75 Unique Items', 'crafting_table', False, 4],



        'X0025': ['Find an Ancient City', 'sculk_shrieker', False, 2],
        'D0008': ['Die to Warden', 'sculk_shrieker', True, 3],
        'K0041': ['Kill Warden', 'iron_sword', True, 8],
        'I0095': ['Obtain Recovery Compass', 'recovery_compass', False, 5],
        'I0096': ['Obtain Mud Brick Wall', 'mud_brick_wall', False, 2],
        'I0097': ['Obtain Froglight', 'pearlescent_froglight', False, 4],
        'I0098': ['Obtain All Froglights', 'pearlescent_froglight', True, 8],
        'I0099': ['Obtain Fermented Spider Eye', 'fermented_spider_eye', False, 3],
        # 'T0010': ['Befriend Allay', 'amethyst_shard', True, 5],
        'B0022': ['Breed Frog', 'slime_ball', True, 4],

        

        'I0100': ['Obtain Brush', 'brush', False, 1],
        'I0101': ['Obtain Armadillo Scute', 'armadillo_scute', True, 2],
        'I0102': ['Apply 3 Unique Armor Trims', 'coast_armor_trim_smithing_template', True, 4],
        'I0103': ['Apply 5 Unique Armor Trims', 'rib_armor_trim_smithing_template', True, 6],
        'I0104': ['Apply 7 Unique Armor Trims', 'silence_armor_trim_smithing_template', True, 8],
        'A0026': ['Apply Armor Trim', 'coast_armor_trim_smithing_template', True, 2],
        'B0023': ['Breed Sniffer', 'sniffer_egg', True, 9],
        'B0024': ['Breed Armadillo', 'spider_eye', True, 4],
        'X0026': ['Locate Trail Ruins', 'brush', False, 3],



        'I0105': ['Obtain Mace', 'mace', False, 10],
        'I0106': ['Obtain Creaking Heart', 'creaking_heart', False, 6],
        'I0107': ['Obtain Resin Brick Stairs', 'resin_brick_stairs', False, 3],
        'A0027': ['Open Trial Vault', 'trial_key', False, 1],
        'A0028': ['Repair Wolf Armor', 'wolf_armor', False, 2],
        'A0029': ['Open Ominous Vault', 'ominous_trial_key', False, 2],
        'A0030': ['Ride Horse', 'saddle', False, 3],
        'K0042': ['Kill Bogged', 'iron_sword', True, 4],
        'K0043': ['Kill Breeze', 'iron_sword', True, 4],
        # 'T0011': ['Tame Every Wolf Variant', 'bone', True, 9],
        # 'T0012': ['Tame 3 Wolf Variants', 'bone', True, 5],
        'D0009': ['Die to Creaking', 'creaking_heart', True, 5],



        'I0108': ['Obtain All Copper Tools', 'copper_pickaxe', True, 1],
        'I0109': ['Obtain Full Copper Armor', 'copper_chestplate', True, 2],
        'I0110': ['Obtain Dried Ghast', 'dried_ghast', False, 3],


        #opponent goals
        'N0001': ['Opponent Obtains Crafting Table', 'barrier', True, 2],
        'N0002': ['Opponent Obtains Obsidian', 'barrier', True, 2],
        'N0003': ['Opponent Obtains Seeds', 'barrier', True, 2],
        'N0004': ['Opponent Eats', 'barrier', True, 2],
        'N0005': ['Opponent Obtains Advancement', 'barrier', True, 4],
        'N0006': ['Opponent Gets 5 Levels', 'barrier', True, 4],
        'N0007': ['Opponent Touches Water', 'barrier', True, 3],
        'N0008': ['Opponent Stands on Netherrack', 'barrier', True, 4],
        'N0009': ['Opponent Stands on Stone', 'barrier', True, 4],
        'N0010': ['Opponent Wears Armor', 'barrier', True, 4],
        'N0011': ['Opponent Dies', 'barrier', True, 2],
        'N0012': ['Opponent Dies 3 Times', 'barrier', True, 2],
        'N0013': ['Opponent Takes 100 Damage', 'barrier', True, 2],
        'N0014': ['Opponent Takes Fall Damage', 'barrier', True, 2],
        'N0015': ['Opponent Catches Fire', 'barrier', True, 2],


        #music discs

        'I1001': ['Obtain Music Disc 5', 'music_disc_5', False, 6],
        'I1002': ['Obtain Music Disc 11', 'music_disc_11', False, 5],
        'I1003': ['Obtain Music Disc 13', 'music_disc_13', False, 4],
        'I1004': ['Obtain Music Disc Blocks', 'music_disc_blocks', False, 5],
        'I1005': ['Obtain Music Disc Cat', 'music_disc_cat', False, 2],
        'I1006': ['Obtain Music Disc Chirp', 'music_disc_chirp', False, 7],
        'I1007': ['Obtain Music Disc Creator', 'music_disc_creator', False, 4],
        'I1008': ['Obtain Creator Music Box', 'music_disc_creator_music_box', False, 4],
        'I1009': ['Obtain Music Disc Far', 'music_disc_far', False, 5],
        'I1010': ['Obtain Music Disc Mall', 'music_disc_mall', False, 5],
        'I1011': ['Obtain Music Disc Mellohi', 'music_disc_mellohi', False, 5],
        'I1012': ['Obtain Music Disc Otherside', 'music_disc_otherside', False, 6],
        'I1013': ['Obtain Music Disc Pigstep', 'music_disc_pigstep', False, 5],
        'I1014': ['Obtain Music Disc Precipice', 'music_disc_precipice', False, 5],
        'I1015': ['Obtain Music Disc Relic', 'music_disc_relic', False, 7],
        'I1016': ['Obtain Music Disc Stal', 'music_disc_stal', False, 5],
        'I1017': ['Obtain Music Disc Strad', 'music_disc_strad', False, 5],
        'I1018': ['Obtain Music Disc Wait', 'music_disc_wait', False, 5],
        'I1019': ['Obtain Music Disc Ward', 'music_disc_ward', False, 5],


        #kill sheep
        'K1001': ['Kill White Sheep', 'white_wool', True, 1], 
        'K1002': ['Kill Pink Sheep', 'pink_wool', True, 1], 
        'K1003': ['Kill Magenta Sheep', 'magenta_wool', True, 1], 
        'K1004': ['Kill Red Sheep', 'red_wool', True, 1], 
        'K1005': ['Kill Orange Sheep', 'orange_wool', True, 1], 
        'K1006': ['Kill Yellow Sheep', 'yellow_wool', True, 1], 
        'K1007': ['Kill Lime Sheep', 'lime_wool', True, 3], 
        'K1008': ['Kill Green Sheep', 'green_wool', True, 3], 
        'K1009': ['Kill Cyan Sheep', 'cyan_wool', True, 3], 
        'K1010': ['Kill Light Blue Sheep', 'light_blue_wool', True, 1], 
        'K1011': ['Kill Blue Sheep', 'blue_wool', True, 1], 
        'K1012': ['Kill Purple Sheep', 'purple_wool', True, 1], 
        'K1013': ['Kill Brown Sheep', 'brown_wool', True, 3], 
        'K1014': ['Kill Light Gray Sheep', 'light_gray_wool', True, 1], 
        'K1015': ['Kill Gray Sheep', 'gray_wool', True, 1], 
        'K1016': ['Kill Black Sheep', 'black_wool', True, 1], 


        #concrete 
        'I2001': ['Obtain 64 White Concrete', 'white_concrete', False, 1], 
        'I2002': ['Obtain 64 Pink Concrete', 'pink_concrete', False, 1], 
        'I2003': ['Obtain 64 Magenta Concrete', 'magenta_concrete', False, 1], 
        'I2004': ['Obtain 64 Red Concrete', 'red_concrete', False, 1], 
        'I2005': ['Obtain 64 Orange Concrete', 'orange_concrete', False, 1], 
        'I2006': ['Obtain 64 Yellow Concrete', 'yellow_concrete', False, 1], 
        'I2007': ['Obtain 64 Lime Concrete', 'lime_concrete', False, 3], 
        'I2008': ['Obtain 64 Green Concrete', 'green_concrete', False, 3], 
        'I2009': ['Obtain 64 Cyan Concrete', 'cyan_concrete', False, 3], 
        'I2010': ['Obtain 64 Light Blue Concrete', 'light_blue_concrete', False, 1], 
        'I2011': ['Obtain 64 Blue Concrete', 'blue_concrete', False, 1], 
        'I2012': ['Obtain 64 Purple Concrete', 'purple_concrete', False, 1], 
        'I2013': ['Obtain 64 Brown Concrete', 'brown_concrete', False, 3], 
        'I2014': ['Obtain 64 Light Gray Concrete', 'light_gray_concrete', False, 1], 
        'I2015': ['Obtain 64 Gray Concrete', 'gray_concrete', False, 1], 
        'I2016': ['Obtain 64 Black Concrete', 'black_concrete', False, 1], 


        
        #glazed terracotta
        'I3001': ['Obtain White Glazed Terracotta', 'white_glazed_terracotta', False, 1], 
        'I3002': ['Obtain Pink Glazed Terracotta', 'pink_glazed_terracotta', False, 1], 
        'I3003': ['Obtain Magenta Glazed Terracotta', 'magenta_glazed_terracotta', False, 1], 
        'I3004': ['Obtain Red Glazed Terracotta', 'red_glazed_terracotta', False, 1], 
        'I3005': ['Obtain Orange Glazed Terracotta', 'orange_glazed_terracotta', False, 1], 
        'I3006': ['Obtain Yellow Glazed Terracotta', 'yellow_glazed_terracotta', False, 1], 
        'I3007': ['Obtain Lime Glazed Terracotta', 'lime_glazed_terracotta', False, 3], 
        'I3008': ['Obtain Green Glazed Terracotta', 'green_glazed_terracotta', False, 3], 
        'I3009': ['Obtain Cyan Glazed Terracotta', 'cyan_glazed_terracotta', False, 3], 
        'I3010': ['Obtain Light Blue Glazed Terracotta', 'light_blue_glazed_terracotta', False, 1], 
        'I3011': ['Obtain Blue Glazed Terracotta', 'blue_glazed_terracotta', False, 1], 
        'I3012': ['Obtain Purple Glazed Terracotta', 'purple_glazed_terracotta', False, 1], 
        'I3013': ['Obtain Brown Glazed Terracotta', 'brown_glazed_terracotta', False, 3], 
        'I3014': ['Obtain Light Gray Glazed Terracotta', 'light_gray_glazed_terracotta', False, 1], 
        'I3015': ['Obtain Gray Glazed Terracotta', 'gray_glazed_terracotta', False, 1], 
        'I3016': ['Obtain Black Glazed Terracotta', 'black_glazed_terracotta', False, 1], 



        # candles
        'I4001': ['Obtain White Candle', 'white_candle', False, 1], 
        'I4002': ['Obtain Pink Candle', 'pink_candle', False, 1], 
        'I4003': ['Obtain Magenta Candle', 'magenta_candle', False, 1], 
        'I4004': ['Obtain Red Candle', 'red_candle', False, 1], 
        'I4005': ['Obtain Orange Candle', 'orange_candle', False, 1], 
        'I4006': ['Obtain Yellow Candle', 'yellow_candle', False, 1], 
        'I4007': ['Obtain Lime Candle', 'lime_candle', False, 3], 
        'I4008': ['Obtain Green Candle', 'green_candle', False, 3], 
        'I4009': ['Obtain Cyan Candle', 'cyan_candle', False, 3], 
        'I4010': ['Obtain Light Blue Candle', 'light_blue_candle', False, 1], 
        'I4011': ['Obtain Blue Candle', 'blue_candle', False, 1], 
        'I4012': ['Obtain Purple Candle', 'purple_candle', False, 1], 
        'I4013': ['Obtain Brown Candle', 'brown_candle', False, 3], 
        'I4014': ['Obtain Light Gray Candle', 'light_gray_candle', False, 1], 
        'I4015': ['Obtain Gray Candle', 'gray_candle', False, 1], 
        'I4016': ['Obtain Black Candle', 'black_candle', False, 1], 


        #stained glass
        'I5001': ['Obtain White Stained Glass', 'white_stained_glass', False, 1], 
        'I5002': ['Obtain Pink Stained Glass', 'pink_stained_glass', False, 1], 
        'I5003': ['Obtain Magenta Stained Glass', 'magenta_stained_glass', False, 1], 
        'I5004': ['Obtain Red Stained Glass', 'red_stained_glass', False, 1], 
        'I5005': ['Obtain Orange Stained Glass', 'orange_stained_glass', False, 1], 
        'I5006': ['Obtain Yellow Stained Glass', 'yellow_stained_glass', False, 1], 
        'I5007': ['Obtain Lime Stained Glass', 'lime_stained_glass', False, 3], 
        'I5008': ['Obtain Green Stained Glass', 'green_stained_glass', False, 3], 
        'I5009': ['Obtain Cyan Stained Glass', 'cyan_stained_glass', False, 3], 
        'I5010': ['Obtain Light Blue Stained Glass', 'light_blue_stained_glass', False, 1], 
        'I5011': ['Obtain Blue Stained Glass', 'blue_stained_glass', False, 1], 
        'I5012': ['Obtain Purple Stained Glass', 'purple_stained_glass', False, 1], 
        'I5013': ['Obtain Brown Stained Glass', 'brown_stained_glass', False, 3], 
        'I5014': ['Obtain Light Gray Stained Glass', 'light_gray_stained_glass', False, 1], 
        'I5015': ['Obtain Gray Stained Glass', 'gray_stained_glass', False, 1], 
        'I5016': ['Obtain Black Stained Glass', 'black_stained_glass', False, 1], 


        #status effects
        'X1025': ['Get Absorption', 'golden_apple', True, 2],
        'X1026': ['Get Glowing', 'spectral_arrow', True, 2],
        'X1027': ['Get Poisoned', 'spider_eye', True, 1],
        'X1028': ['Get Nausea', 'pufferfish', True, 3],
        'X1029': ['Get Leaping', 'rabbit_foot', False, 2],
        'X1030': ['Get Withered', 'wither_rose', False, 3],
        'X1031': ['Get Mining Fatigue', 'wooden_shovel', True, 3],
        'X1032': ['Get Blindness', 'suspicious_stew', False, 3],
        'X1033': ['Get Strength', 'blaze_powder', False, 5],
        'X1034': ['Get Fire Resistance', 'potion', True, 4],
        'X1035': ['Get Water Breathing', 'potion', True, 3],
        'X1036': ['Get Night Vision', 'potion', True, 2],
        'X1037': ['Get Weakness', 'wooden_sword', True, 2],


        #goal ideas
        # "X0011": ['Fill Inventory with Unique Items', '"id": "minecraft:chest"', 1],
        # "X0013": ['Get a Villager to Max Level', '"id": "minecraft:emerald"', 3],
        # "X0022": ['Use Banner Pattern on Banner', '"id": "minecraft:flow_banner_pattern"', 1],
        # "X0034": ['Create Rainbow Sheep', '"id": "minecraft:nametag"', 2],
        # "X0035": ['Summon Johnny', '"id": "minecraft:nametag"', 3],
        # "L0014": ['Find a Badlands Biome', '"id": "minecraft:terracotta"', 3],
}



def parseGoalPool(poolId) -> list:
    try:
        file = open('goal_pools/' + poolId + '.json', 'r')
        goalPool = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print('The specified goal pool,', poolId, ', could not be found or is unreadable.') 
        print(e)
        return []

    goalList = []

    for pool in goalPool['pools']:
        type = pool['type']

        if type == 'all':
            for goal in pool['goals']:
                goalList.append(goal)
        elif type == 'weighted':
            for goal in pool['goals']:
                pass #TODO: Implement weighted goal parser
        elif type == 'pick':
            for _ in range(pool['amount']):
                randomGoal = random.choice(pool['goals'])
                goalList.append(randomGoal)
                pool['goals'].remove(randomGoal) #ensure the same goal is not picked twice
        else:
            continue

    return goalList
    


if __name__ == '__main__':
    print("Goals:", len(goalIndex))
    # for goal in goalIndex:
    #     print(f'"{goal}",')

