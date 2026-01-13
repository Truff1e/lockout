![Alt text](assets/banner.png)

# Truffle's Minecraft Lockout Generator
![GitHub Release](https://img.shields.io/github/v/release/truff1e/lockout)
![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/truff1e/lockout/total)


## What is Lockout?
Minecraft Lockout is a game in which two teams compete to complete as many goals as they can on a board of 25 goals. The goals can be as simple as 'Eat Apple' or as challenging as 'Enter End City'. Each goal is worth one point. When one team completes a goal, the other team is "locked out" of that goal and can no longer earn a point for it. The first team to complete more than half the board wins.

This game was originally invented by SmallAnt and created by AtSign as a Forge mod. This code generates data packs that can be played in 100% vanilla Minecraft. 

You can find the original mod on Curseforge [here](https://www.curseforge.com/minecraft/mc-mods/lockout).
Credit for the concept goes to SmallAnt - [Check out his YouTube channel!](https://www.youtube.com/@Smallant)

I hope you enjoy!

~Truffle

## How It Works
This generator creates a data pack for each lockout board. There are two different ways to create a board.

- balanced (Automatically generates a board with balanced difficulty. This is the recommended option when starting out.)

- custom (You specify what goals are on your board using a list of goal ID keys)

To get started, download or clone this repo using the green Code button. If you downloaded, extract the ZIP somewhere convenient, then open a terminal and navigate to that directory. You must have python installed on your system. To get going quickly, simply write `python3 lockout.py` and your data pack should appear in your Downloads folder. Drag the file into your world's datapacks folder, and you are good to go! No need to unzip. For more detailed instructions, read on.


### Generate a Balanced Board (Start here!)
Running `python3 lockout.py` in a terminal will create a random 5x5 board balanced to a reasonable difficulty. This is the recommended option if you are just starting out or want to start playing quickly.
You can customize several options when generating a board. For example, the command below will make a 4x4 board with a maximum difficulty of 6/10:
```python3 lockout.py -s 4 -d 1-6```

For the help page, run 
```python3 lockout.py --help```

The length of your game depends on the board size and the difficulty you choose.
I recommend a 3 or 4 size board for short games (45m-1hr), and 5 or 6 for longer games (1.5-2hrs).
In theory, the board can be as big as you want, although the generator may crash if you try to create a board with more goals than exist. I wouldn't recommend going above 12x12.

The difficulty range is set by any two integers between 1 and 10 separated by a hyphen (-). The larger number (max difficulty) comes second.

Running `python3 lockout.py -d 1-3` gives you a very easy board, with goals that are rated between 1/10 and 3/10 difficulty.


### Generate a Custom Board
To manually create a board, you need to create a list of goal ID numbers. You can look through index.py to see a complete list of all the available goals.

When you have slected your goals, put the ID numbers in a space-separated list.
For example: A0001 A0002 A0003 etc. Do not put the same goal in the list twice, it will cause problems.
You also must have a square number of goals (4, 9, 16, 25, 36, etc.)

Run the command 
```python3 lockout.py -b custom <yourlistofgoals>```

Your data pack will appear by default in your Downloads folder.


## Installing the Data Pack and Playing Lockout
To install a data pack, open your Minecraft world folder and find the folder labeled 'datapacks'. Drag the zip file into this folder (no need to extract it), then run /reload in your world.

To play lockout, install the data pack on your world or on a server. Add players to teams using `/team join 1 <player>` and `/team join 2 <player>`.
You can change the colors of the teams by typing `/team modify 1 color <color>`.
To start the game, run  
```/function lockout:game/start``` 
If a player joins late, and they can't see the lockout board, first add them to a team and have them relog.

## Limitations
Typically in lockout, you have a compass to track players. However, a compass is clunky to implement in a data pack, so instead you can use `/trigger locate` at any time to see players' coordinates during the game. In newer Minecraft versions, you can use the locator bar as well.

There is no lockout board overlay like in the original mod. Press your advancements keybind (default is L) to see the lockout board. 

**WARNING: Do not install this data pack on a pre-existing world. Lockout is intended to be played on a new world with a random seed.**

With that being said, there are plenty of benefits to playing in vanilla. You can install any mods you want and your friends can join and play instantly without any tricky client-side setup.

## Playing Blackout
The data pack also allows you to start a Blackout game (like lockout except everyone is on the same team and you try to complete the entire board)

To play, follow the same steps as above to generate the data pack and load it into your world. Then run `/reload` and either click the button in chat that says START BLACKOUT or type 
```/function lockout:game/start_blackout```


## Resource Pack
In order to make some of the goal icons more descriptive, this generator comes with an optional resource pack that utilizes some of the textures from the original lockout mod. You do not have to do any setup besides enabling it on your client. If you know how, you can set it as the server resource pack.


## Known Issues
Due to data pack limitations, there may be some issues with players logging off during the game, though I've done as much as I can to limit any problems from this. One such issue that may arise is if a player logs out during the game start sequence. If this happens and the player cannot move/jump after the game has started, try running `/execute as <affected_player> run function lockout:game/reset_attributes`


## License
This code is licensed under the terms of the GNU GPLv3 license.

Derivative works must also be licensed under the GPL.
