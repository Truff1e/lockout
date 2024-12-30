from tkinter import *
from lockout import *
from tkinter import ttk

def generatebalanced():
    if not blackoutvar.get():
        balancedboard(int(sizevar.get()//1)**2, str(difficultyvar.get().__round__(1)).split(','), overridesvar.get().lower().strip('% ').split(','))
    else:
        balancedboard(int(sizevar.get()//1)**2, str(difficultyvar.get().__round__(1)).split(','), overridesvar.get().lower().strip('% ').split(','), excluded=['opponent'])
    exit()

def generaterandom():
    randomboard(int(sizevar.get()//1)**2, overridesvar.get().lower().strip('% ').split(','))
    exit()

def generatecustom():
    customboard(customboardtext.get("1.0", "end-1c").strip(" ").split(','))
    exit()

def getsizesildervalue():
    return int(sizevar.get()//1)

def getrandomsizesildervalue():
    return int(randomsizevar.get()//1)

def getdifficultysildervalue():
    return '{: .1f}'.format(difficultyvar.get())

def randomgoal():
    goal = getrandomgoal()
    return f"{goal} - {goalDictionary[goal][0]}"


# Window
window = Tk()
window.title("Lockout Generator")
window.geometry("350x300")
window.resizable(0,0)

window.iconphoto(True, PhotoImage(file='assets/logo1024.png'))

# Notebook Windows
notebook = ttk.Notebook(window)

custom_generator = ttk.Frame(window)
balanced_generator = ttk.Frame(window)
random_generator = ttk.Frame(window)
goaltranslator = ttk.Frame(window)


# Variables
sizevar = DoubleVar()
sizevar.set(5)
blackoutvar = BooleanVar()
blackoutvar.set(False)
randomsizevar = DoubleVar()
randomsizevar.set(5)
difficultyvar = DoubleVar()
difficultyvar.set(4)
overridesvar = StringVar()
customgoallistvar = StringVar()
translatevar = StringVar()
goalidvar = StringVar()


# Balanced Board
boardsize = ttk.Frame(balanced_generator, padding=5)
difficulty = ttk.Frame(balanced_generator, padding=5)
overrides = ttk.Frame(balanced_generator, padding=5)

ttk.Label(boardsize, text="Board Size: ").pack(side=LEFT)
boardsizeslider = ttk.Scale(boardsize, from_=1, to=9, orient='horizontal', variable=sizevar, command=(lambda event: boardsizelabel.configure(text=f"{getsizesildervalue()} x {getsizesildervalue()}")))
boardsizelabel = ttk.Label(boardsize, text=f"{getsizesildervalue()} x {getsizesildervalue()}")
boardsizeslider.pack(side=LEFT, padx=10, pady=3)
boardsizelabel.pack(side=LEFT)
ttk.Label(difficulty, text="Difficulty: ").pack(side=LEFT)
difficultyslider = ttk.Scale(difficulty, from_=1, to=8, orient='horizontal', variable=difficultyvar, command=(lambda event: difficultylabel.configure(text=f"{getdifficultysildervalue()}")))
difficultylabel = ttk.Label(difficulty, text=getdifficultysildervalue())
difficultyslider.pack(side=LEFT, padx=10, pady=3)
difficultylabel.pack(side=LEFT)
# Label(overrides, text="Overrides: ").pack(side=LEFT)
# Entry(overrides, textvariable=overridesvar).pack(side=LEFT)
blackouttoggle = ttk.Checkbutton(balanced_generator, text="Blackout Mode", variable=blackoutvar, padding=10)
generatebutton = ttk.Button(balanced_generator, text="Generate Balanced Board", command=generatebalanced)

boardsize.pack()
difficulty.pack()
# overrides.pack()
blackouttoggle.pack()
generatebutton.pack()


# Random Board
randomboardsize = ttk.Frame(random_generator, padding=5)
randomoverrides = ttk.Frame(random_generator, padding=5)

ttk.Label(randomboardsize, text="Board Size: ").pack(side=LEFT)
randomboardsizeslider = ttk.Scale(randomboardsize, from_=1, to=9, orient='horizontal', variable=randomsizevar, command=(lambda event: randomboardsizelabel.configure(text=f"{getrandomsizesildervalue()} x {getrandomsizesildervalue()}")))
randomboardsizelabel = ttk.Label(randomboardsize, text=f"{getsizesildervalue()} x {getsizesildervalue()}")
randomboardsizeslider.pack(side=LEFT, padx=10, pady=3)
randomboardsizelabel.pack(side=LEFT)
# Label(randomoverrides, text="Overrides: ").pack(side=LEFT)
# Entry(randomoverrides, textvariable=overridesvar).pack(side=LEFT)
randomgeneratebutton = ttk.Button(random_generator, text="Generate Random Board", command=generaterandom)

randomboardsize.pack()
# randomoverrides.pack()
randomgeneratebutton.pack()


# Custom Board
customboardinput = ttk.Frame(custom_generator, padding=10)
ttk.Label(customboardinput, text="Custom Board: ").pack(side=LEFT)
customboardtext = Text(customboardinput, height=7, width=25)
customboardtext.pack(side=LEFT)
customgeneratebutton = ttk.Button(custom_generator, text="Generate Custom Board", command=generatecustom)

customboardinput.pack()
customgeneratebutton.pack()


# Goal Translator
translate_goal = ttk.Frame(goaltranslator, padding=5)
ttk.Button(translate_goal, text="Translate", command=(lambda: outputlabel.config(text=f"Goal Name is: {translate(translatevar.get())}"))).pack(side=LEFT)
Entry(translate_goal, textvariable=translatevar).pack(side=LEFT)
getgoalID = ttk.Frame(goaltranslator, padding=5)
ttk.Button(getgoalID, text="Get Goal ID", command=(lambda: outputlabel.config(text=f"Goal ID is: {getid(goalidvar.get())}"))).pack(side=LEFT)
Entry(getgoalID, textvariable=goalidvar).pack(side=LEFT)

translate_goal.pack()
getgoalID.pack()
ttk.Button(goaltranslator, text="Get Random Goal", command=(lambda: outputlabel.config(text=randomgoal())), padding=5).pack()
outputlabel = ttk.Label(goaltranslator, padding=8, font=("Arial", 14), text="No input")
outputlabel.pack()

# Notebook Packing
notebook.add(balanced_generator, text="Balanced")
notebook.add(random_generator, text="Random")
notebook.add(custom_generator, text="Custom")
notebook.add(goaltranslator, text="Goals")

appicon = PhotoImage(file="assets/app_splash.png")
Label(window, image=appicon, pady=15).pack()
Label(window, text="v1.7.3 - Created by Truff1e", pady=3).pack()
notebook.pack()

window.mainloop()
