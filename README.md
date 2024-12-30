# Lockout Generator v1.7.4

## What is Lockout?
Minecraft Lockout is a game in which two teams compete to complete as many goals as they can on a 5x5 board. The goals could be as simple as 'Ride a Horse' or as challenging as 'Kill the Ender Dragon'. Each goal is worth one point, and if one team completes a goal, the other team can no longer get a point for that goal. First team to complete the majority of the board wins.

This game was originally invented by SmallAnt and created by AtSign as a Forge mod. This version is a data pack which means it can be played in 100% vanilla Minecraft and no client-side installations are necessary. 

You can find the original mod on curseforge [here](https://www.curseforge.com/minecraft/mc-mods/lockout).
All credit for the game concept goes to SmallAnt - [Check out his YouTube!](https://www.youtube.com/@Smallant)

I hope you enjoy!
~Truffle

## How to Generate a Board
To begin, make sure you have python installed and then run gui.py. To generate a board, you can use any of the three presets:

balancedboard - Generates a board with weighted difficulty distribution for optimal gameplay balance. This is the recommended option for starting out. 

randomboard - Generates a completely random board with wildly varying ranges of difficulty

customboard - Generates a user-specified board using a provided list of goal ID numbers



### GENERATE A BALANCED BOARD (RECOMMENDED - START HERE)
The balancedboard command will create a fair and fun board weighed to the specified difficulty. This is the recommended option if you are just starting out or just want to start playing quickly.
To create a balanced board, set the board size and difficulty using the sliders, and click "generate board". Leave the overrides field blank - more about that below.

The length of your game heavily depends on this board size and the difficulty you choose.
I recommend a 3 or 4 size board for short games (45m-1hr), and 5 for longer games (1.5-2hrs).  


### CREATE A CUSTOM BOARD
To manually create a board, look through index.py and find a bunch of goals you want to have on your board. Put the ID number of these goals in a comma-separated list with no spaces.
For example: A0001,A0002,A0003,etc. Do not put the same goal in the list twice, it will cause your data pack not to work properly.


The "goals" tab has some helpful commands for finding specific goals.


### GENERATE A RANDOM BOARD
To generate a completely random board, specify a size and then click generate. I highly reccommend using balanced board instead of this option.


### OUTPUT
Your data pack will generate in the folder "datapacks" and you can see what goals were added in the console.


## Installing the Data Pack and Playing Lockout
To install a data pack, open your Minecraft world folder and find the folder labeled 'datapacks'. Drag the zip file into this folder (no need to unzip it), then run /reload in your world.

To play lockout, first install the data pack on your world or on a server. Add players to teams using "/team join 1 <player>" and "/team join 2 <player>".
You can change the colors of the teams by typing "/team modify 1 color <color>".
To start the game, run "/function lockout:game/start". If a player joins late, and they can't see the lockout board, type "/function lockout:game/resume" (this should happen automatically as of v1.3.0, however if this is the first time the player is joining, they will have to relog again to reset)

## Limitations

Since a compass tracker is hard to implement in a data pack, instead you can use "/trigger locate" to see any player's coordinates in the world.

There is no lockout board overlay like in the original mod. Press your advancements keybind (defaults to L) to see the lockout board. 

There is also no way for the data pack to detect what the seed will be like, so there is no gaurentee that every goal is completable within 2000 blocks.

**Do not install this data pack on a pre-existing world. Lockout is intended to be played on a new world with a random seed.**

With that being said, there are plenty of benefits to playing in vanilla. You can install any mods you want and your friends can join and play instantly without any annoying client-side setup. If you have any questions, stay tuned for my video covering how to use the generator and play the game. 

## Playing Blackout

The data pack also allows you to start a Blackout game (same as a lockout except everyone is on the same team and you try to complete the entire board)

To play, follow the same steps as above to generate the data pack and load it into your world. Then run /reload and either click the button in chat that says START BLACKOUT or type /function lockout:game/start_blackout


## Resource Pack
In order to make some of the goal icons more descriptive, this generator comes with an optional resource pack that utilizes some of the textures from the original lockout mod. The file is in the data packs folder, and you do not have to do any setup besides enabling it on your client.


## Known Issues
'Whatever Floats your Goat' advancement does not work and is not counted for unique advancements goal.

Due to data pack limitations, there may be some issues with players logging off during the game, though I've done as much as I can to limit any problems from this. One such issue that may arise is if a player logs out during the game start sequence. If this happens and the player cannot move/jump after the game has started, try running "/execute as <affected_player> run function lockout:game/reset_attributes"


## License
This code is licensed under terms of the GNU GPLv3 license.
You may use this code for your own personal enjoyment. Do not distribute this code for profit without significant customizations and changes.
