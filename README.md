# Lockout Generator v1.7.0

Minecraft Lockout is a game in which two teams compete to complete as many goals as they can on a 5 by 5 board. The goals could be as simple as 'Ride a Horse' or as challenging as 'Kill the Ender Dragon'. If one team completes a goal, the other team can no longer get points for that goal. First team to complete the majority of the board wins.

This game was originally invented by SmallAnt and created by AtSign as a Forge mod. This version is a data pack which means it can be played in 100% vanilla Minecraft and no client-side installations are necessary. 

You can find the original mod here: https://www.curseforge.com/minecraft/mc-mods/lockout
All credit for the game concept goes to SmallAnt.

I hope you enjoy!
~Truffle

Warning: Do not tamper with the 'template' folder unless you know what you are doing. It could cause your data packs to break.

## How to Generate a Board
To begin, make sure you have python installed and then run lockout.py. To generate a board, you can use any of the three following commands:

balancedboard - Generates a board with weighted difficulty distribution for optimal gameplay balance. This is the recommended option for starting out. 

randomboard - Generates a completely random board with wildly varying ranges of difficulty

customboard - Generates a user-specified board using a provided list of goal ID numbers

#### MANUALLY CREATE A BOARD
To manually create a board, look through index.py and find a bunch of goals you want to have on your board. Put these goals in a comma-separated list with no spaces.
For example: A0001,A0002,A0003,etc. Do not put the same goal in the list twice, it will cause your data pack not to work properly. To generate the custom board, type: 

**customboard *size* *goals***

*Size* is how big you want your board to be. Put 5 for a 5x5 board, 6 for a 6x6 board, etc. You can make up to a 9x9 board.

*Goals* is the list of goals you have chosen above.


Some helpful commands for finding specific goals are:

'translate _goalID_' - This command translates a Goal ID into that goal's name. For example, K0001 would translate to "Kill 100 Mobs".

'getid _name_of_goal_' - This command does the opposite of the 'translate' command. You input a goal name, and get that goal's ID.

'getrandomgoals _amount_' - Alternatively to the two previous commands, you can use this command to retrieve an amount of randomly selected goals.


#### GENERATE A RANDOM BOARD
To generate a completely random board, run the command 'randomboard {board_size}'


#### GENERATE A BALANCED BOARD (RECOMMENDED)
The balancedboard command will create a fair and fun board weighed to the specified difficulty. This is the recommended option if you are just starting out or just want to start playing quickly.
To create a balanced board, run the command 'balancedboard'. 

**balancedboard *size* *difficulty***

*Size* is how big you want your board to be. Put 5 for a 5x5 board, 6 for a 6x6 board, etc. You can make up to a 9x9 board.

*Difficulty* can be either a decimal number between 1 and 7 or a set of weighted values if you want extra customization. The easiest method is to just use the built-in difficulty calculator by inputting a number between 1 and 7, decimals included. 7 will be the hardest, while 1 will be the easiest. For more advanced options, see the section below.

The length of your game heavily depends on this board size and the difficulty you choose.
I recommend a 3 or 4 size board for short games (45m-1hr), and 5 for longer games (1.5-2hrs).  


Example Command (good for beginners):
*$balancedboard 5 2.2*

Example Command with Overrides:
*$balancedboard 4 3.5 %sheep,netherite


#### SET A CUSTOM DIFFICULTY
If you wish to set your own custom weights, you will need to
understand the goal difficulty ranking.
Lvl 1 Goals - These goals are extremely easy and can be completed within the first 10-20 minutes of the game. For example, Obtain All Stone Tools.
Lvl 2 Goals - These goals are a little harder and will require you to do a bit of prep beforehand. For example, Breed Strider is a lvl 2 goal.
Lvl 3 Goals - These goals are very hard and will take a lot of time to complete. For example, Obtain Netherite Armor
Lvl 4 Goals - These goals are extremely hard and most of the time require you to go to the end. These probably aren't suited for a 1.5-2hr game.

To input a custom difficulty, just type a list of weights like this: 8,5,5,2 Each number corresponds to the frequency that difficulty of goal 
will show up. Approximately 8/20 goals will be level 1 difficulty, 5/20 will be level 2, 5/20 will be level 3 and 2/20 will be level 4.

Finally, you can specify if you would like to override any of the exclusive sets for the goal index. These exclusive sets prevent similar 
goals from showing up twice in the same board - for example, one set makes sure you don't have "Kill Red Sheep", "Kill Cyan Sheep" and 
"Kill Yellow Sheep" all on the same board. Doing nothing will activate all the exclusive sets. If you want to override all 
sets, type '%all' after either the balancedboard or randomboard command. If you want to override specific sets, first type "%", then type the name(s) of the set(s) separated by commas. You can find all the exclusive sets at 
the bottom of index.py

Example command:
*$balancedboard 5 4,4,3,2 %concrete,effects*

Your data pack will generate in the folder "datapacks" and you can see what goals were added in the console.


## Installing the Data Pack and Playing Lockout
To install a data pack, open your Minecraft world folder and find the folder labeled 'datapacks'. Drag the zip file into this folder, then run /reload in your world.

To play lockout, first install the data pack on your world or on a server. Add players to teams using "/team join 1 <player>" and "/team join 2 <player>".
You can change the colors of the teams by typing "/team modify 1 color <color>".
To start the game, run "/function lockout:game/start". If a player joins late, and they can't see the lockout board, type "/function lockout:game/resume" (this should happen automatically as of v1.3.0 if the player relogs)

## Limitations

Since a compass tracker is hard to implement in a data pack, instead you can use "/trigger locate" to see any player's coordinates in the world.

There is no lockout board overlay like in the original mod. Press your advancements keybind (defaults to L) to see the lockout board. 

There is also no way for the data pack to detect what the seed will be like, so there is no gaurentee that every goal is completable within 2000 blocks. A common choke point is finding a desert for green dyes.


Do not install this data pack on a pre-existing world. Lockout is intended to be played on a new world with a random seed.

With that being said, there are plenty of benefits to playing in vanilla. You can install any mods you want and your friends can join and play instantly without any annoying client-side setup. If you have any questions, stay tuned for my video covering how to use the generator and play the game. 

## Playing Blackout

The data pack also allows you to start a Blackout game (same as a lockout except everyone is on the same team and you try to complete the entire board)

To play, follow the same steps as above to generate the data pack and load it into your world. Then run /reload and either click the button in chat that says START BLACKOUT or type /function lockout:game/start_blackout


## Known Issues
'Whatever Floats your Goat' advancement does not work and is not counted for unique advancements goal.


## License
This code is licensed under terms of the GNU GPLv3 license.
