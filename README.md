# Lockout Generator v2.0

## What is Lockout?
Minecraft Lockout is a game in which two teams compete to complete as many goals as they can on a board of 25 goals. The goals could be as simple as 'Ride a Horse' or as challenging as 'Kill the Ender Dragon'. Each goal is worth one point, and when one team completes a goal, the other team can no longer get a point for that goal. First team to complete the majority of the board wins.

This game was originally invented by SmallAnt and created by AtSign as a Forge mod. This version is a data pack so it can be played in vanilla Minecraft with no extra client-side installations. 

You can find the original mod on curseforge [here](https://www.curseforge.com/minecraft/mc-mods/lockout).
All credit for the game concept goes to SmallAnt - [Check out his YouTube!](https://www.youtube.com/@Smallant)

I hope you enjoy!
~Truffle

## How to Generate a Board
To create a data pack, first make sure you have python installed and then run cli.py. You will be greeted with a welcome screen. 

There are two different ways to create a board.

balanced - Generates a board with weighted difficulty distribution for optimal gameplay balance. This is the recommended option for starting out.

custom - Generates a user-specified board using a provided list of goal ID numbers


### Generate a Balanced Board (Start Here)
The "gen b" command will create a fair and fun board weighed to the specified difficulty. This is the recommended option if you are just starting out or want to start playing quickly.
To create a balanced board, type the command 
```gen b <size> <difficultyrange>```
and hit enter. The app should reveal the data pack in your Downloads folder.

The length of your game heavily depends on this board size and the difficulty you choose.
I recommend a 3 or 4 size board for short games (45m-1hr), and 5 or 6 for longer games (1.5-2hrs).

Difficulty range is set by any two integers between 1 and 10 separated by a hyphen (-). The larger number (max difficulty) comes second.

NOTE: Board sizes must be square numbers (9, 16, 25, 36, etc.) otherwise the generator will not work!


### Generate a Custom Board
To manually create a board, you need to make a list of goal ID numbers. Some tools to find goal IDs are explained below. Alternatively, you can look through index.py in the source code to see a list of all available goals.

When you have slected your goals, put the ID numbers in a space-separated list.
For example: A0001 A0002 A0003 etc. Do not put the same goal in the list twice, it will cause your data pack not to work properly.
Again, you must have a square number of goals (4, 9, 16, 25, 36, etc.)

Run the command 
```gen c <yourlistofgoals>```


### Output
Your data pack will generate by default in your Downloads folder.


## Installing the Data Pack and Playing Lockout
To install a data pack, open your Minecraft world folder and find the folder labeled 'datapacks'. Drag the zip file into this folder (no need to extract it), then run /reload in your world.

To play lockout, first install the data pack on your world or on a server. Add players to teams using "/team join 1 <player>" and "/team join 2 <player>".
You can change the colors of the teams by typing "/team modify 1 color <color>".
To start the game, run 
```/function lockout:game/start``` 
If a player joins late, and they can't see the lockout board, add them to a team and have them relog. That should fix the problem.

## Limitations

Since a compass tracker is hard to implement in a data pack, instead you can use "/trigger locate" to see any player's coordinates in the world.

There is no lockout board overlay like in the original mod. Press your advancements keybind (defaults to L) to see the lockout board. 

There is also no way for the data pack to detect what the seed will be like, so there is no gaurentee that every goal is completable within 2000 blocks.

**Do not install this data pack on a pre-existing world. Lockout is intended to be played on a new world with a random seed.**

With that being said, there are plenty of benefits to playing in vanilla. You can install any mods you want and your friends can join and play instantly without any tricky client-side setup. 

## Playing Blackout

The data pack also allows you to start a Blackout game (same as a lockout except everyone is on the same team and you try to complete the entire board)

To play, follow the same steps as above to generate the data pack and load it into your world. Then run /reload and either click the button in chat that says START BLACKOUT or type 
```/function lockout:game/start_blackout```


## Resource Pack
In order to make some of the goal icons more descriptive, this generator comes with an optional resource pack that utilizes some of the textures from the original lockout mod. The file is in the data packs folder, and you do not have to do any setup besides enabling it on your client.


## Known Issues
Due to data pack limitations, there may be some issues with players logging off during the game, though I've done as much as I can to limit any problems from this. One such issue that may arise is if a player logs out during the game start sequence. If this happens and the player cannot move/jump after the game has started, try running "/execute as <affected_player> run function lockout:game/reset_attributes"


## License
This code is licensed under terms of the GNU GPLv3 license.
You may use this code for your own personal enjoyment. Do not distribute this code for profit without significant customizations and changes.
