# Lockout Data Pack Generator

CAUTION: DO NOT TAMPER WITH THE CONTENTS OF THE lockout_template FOLDER. YOUR DATA PACKS WILL NOT WORK IF THIS FOLDER IS MODIFIED OR MOVED!

### How to Generate a Board
To begin, run lockout.py in your command line. You can either:

 - Manually add goals to the board, then generate it
 - Generate a completely random board
 - Generate a balanced board with a specified difficulty.

The instructions for these three options are below:


**MANUALLY CREATE A BOARD**
To manually create a board, simply run lockout.py and then type in either a goal ID (ex: A0001) or a goal name (ex: "Kill 100 Mobs").
Repeat this until you have put in all the goals you want. Please note that you cannot generate a board that is not square.
You must input 1, 4, 9, 25, 36, 49 or 64 goals. It is not recommended to make a board larger than 64 goals. Once you are ready to generate
your board, type 'generate' and a zip file will be created inside the folder ./files/gen. Other useful commands for manually creating a board are:

'del' - This command will delete the last entry into your list. To delete a specific entry, type 'del0' to delete the first goal in the list, 'del1' to delete the second and so on.
'print' - This command will print your list of goals so you can review them or save the list for later.
'printnames' - This command prints your list of goals and their names so you can easily see what goals you have.
'translate' - This command translates a Goal ID into that goal's name. For example, K0001 would translate to "Kill 100 Mobs".
'getid' - This command does the opposite of the translate command. You input a goal name, and get that goal's ID.
'dumpgoals' - Alternatively to the two previous commands, you can use this command to see every single goal ID paired with its name.


**GENERATE A RANDOM BOARD**
To generate a completely random board, run the command 'randomboard', then follow the prompts to input a number of goals. Your data pack will
generate in the folder "./files/gen".


**GENERATE A BALANCED BOARD**
To create a balanced board, first run the command 'balancedboard'. The generator will then ask you for a board size. You may put any square
number (1, 4, 9, 16, 25...) below 100 for your board size. The length of your game heavily depends on this board size and the difficulty you choose.
I recommend a 9 or 16 size board for short games (45m-1hr), and 25 for longer games (1.5-2hrs). The generator will now ask for a difficulty.
You can choose to use the built-in difficulty calculator or put in a custom list of weights. The default difficulties range from 1 to 7 and can be
any decimal number in between. 7 will be the hardest, while 1 will be the easiest. If you wish to set your own custom weights, you will need to
understand the goal difficulty ranking.

Lvl 1 Goals - These goals are extremely easy and can be completed within the first 10-20 minutes of the game. For example, Obtain All Stone Tools.
Lvl 2 Goals - These goals are a little harder and will require you to do a bit of prep beforehand. For example, Breed Strider is a lvl 2 goal.
Lvl 3 Goals - These goals are very hard and will take a lot of time to complete. For example, Obtain Netherite Armor
Lvl 4 Goals - These goals are extremely hard and most of the time require you to go to the end. These probably aren't suited for a 1.5-2hr game.

To input a custom difficulty, just type a list of weights like this: [8, 5, 5, 2] Each number corresponds to the frequency that difficulty of goal 
will show up. Approximately 8/20 goals will be level 1, 5/20 will be level 2, 5/20 will be level 3 and 2/20 will be level 4.

Finally, the data pack will ask if you would like to override any of the exclusive sets for the goal index. These exclusive sets prevent similar 
goals from showing up twice in the same board - for example, one set makes sure you don't have "Kill Red Sheep", "Kill Cyan Sheep" and 
"Kill Yellow Sheep" all on the same board. Pressing enter without typing anything will activate all the exclusive sets. If you want to override all 
sets, type 'all'. If you want to override specific sets, type the name(s) of the set(s) separated by spaces. You can find all the exclusive sets at 
the bottom of index.py

Your data pack will generate in the folder "./files/gen" and you can see what goals were generated in the console.


**INSTALLING THE DATA PACK AND PLAYING LOCKOUT**
To install a data pack, open your Minecraft world folder and find the folder labeled 'datapacks'. Drag the zip file into this folder, then run /reload in your world.

To play lockout, first install the data pack on your world or on a server. Add players to teams using "/team join 1 <player>" and "/team join 2 <player>".
You can change the colors of the teams by typing "/team modify 1 color <color>".
To start the game, run "/function lockout:game/start". If a player joins late, and they can't see the lockout board, type "/function lockout:game/resume" (this should happen automatically as of v1.3.0)
Since a compass tracker is hard to implement in a data pack, instead you can use "/trigger locate" to see player's coordinates in the world.
Press your advancements keybind (defaults to L) to see the lockout board.


Do not install this data pack on a pre-existing world. This data pack is intended to be played on a new world.


I hope you enjoy!
~Truffle