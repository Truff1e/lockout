from tkinter import *
from lockout import balancedboard, randomboard, customboard
from tkinter import ttk

def generatebalanced():
    balancedboard(int(sizevar.get()//1)**2, str(difficultyvar.get()).split(','), overridesvar.get().lower().strip('% ').split(','))
    exit()

def generaterandom():
    randomboard(int(sizevar.get()//1)**2, overridesvar.get().lower().strip('% ').split(','))
    exit()

def generatecustom():
    customboard(customboardtext.get("1.0", "end").lower().strip(" ").split(','))
    exit()


def getsizesildervalue():
    return int(sizevar.get()//1)

def getrandomsizesildervalue():
    return int(randomsizevar.get()//1)

def getdifficultysildervalue():
    return '{: .1f}'.format(difficultyvar.get())


window = Tk()
window.title("Lockout Generator")
window.geometry("350x280")
window.resizable(0,0)

window.iconphoto(True, PhotoImage(file='assets/logo1024.png'))

notebook = ttk.Notebook(window)

custom_generator = ttk.Frame(window)
balanced_generator = ttk.Frame(window)
random_generator = ttk.Frame(window)


sizevar = DoubleVar()
sizevar.set(5)
randomsizevar = DoubleVar()
randomsizevar.set(5)
difficultyvar = DoubleVar()
difficultyvar.set(4)
overridesvar = StringVar()
customgoallistvar = StringVar()

# Balanced Board
boardsize = Frame(balanced_generator, padx=10, pady=5)
difficulty = Frame(balanced_generator, padx=10, pady=5)
overrides = Frame(balanced_generator, padx=10, pady=5)

Label(boardsize, text="Board Size: ").pack(side=LEFT)
boardsizeslider = ttk.Scale(boardsize, from_=1, to=9, orient='horizontal', variable=sizevar, command=(lambda event: boardsizelabel.configure(text=f"{getsizesildervalue()} x {getsizesildervalue()}")))
boardsizelabel = Label(boardsize, text=f"{getsizesildervalue()} x {getsizesildervalue()}")
boardsizeslider.pack(side=LEFT, padx=10, pady=3)
boardsizelabel.pack(side=LEFT)
Label(difficulty, text="Difficulty: ").pack(side=LEFT)
difficultyslider = ttk.Scale(difficulty, from_=1, to=8, orient='horizontal', variable=difficultyvar, command=(lambda event: difficultylabel.configure(text=f"{getdifficultysildervalue()}")))
difficultylabel = Label(difficulty, text=getdifficultysildervalue())
difficultyslider.pack(side=LEFT, padx=10, pady=3)
difficultylabel.pack(side=LEFT)
Label(overrides, text="Overrides: ").pack(side=LEFT)
Entry(overrides, textvariable=overridesvar).pack(side=LEFT)
generatebutton = Button(balanced_generator, text="Generate Balanced Board", command=generatebalanced)

boardsize.pack()
difficulty.pack()
overrides.pack()
generatebutton.pack()


# Random Board
randomboardsize = Frame(random_generator, padx=10, pady=5)
randomoverrides = Frame(random_generator, padx=10, pady=5)

Label(randomboardsize, text="Board Size: ").pack(side=LEFT)
randomboardsizeslider = ttk.Scale(randomboardsize, from_=1, to=9, orient='horizontal', variable=randomsizevar, command=(lambda event: randomboardsizelabel.configure(text=f"{getrandomsizesildervalue()} x {getrandomsizesildervalue()}")))
randomboardsizelabel = Label(randomboardsize, text=f"{getsizesildervalue()} x {getsizesildervalue()}")
randomboardsizeslider.pack(side=LEFT, padx=10, pady=3)
randomboardsizelabel.pack(side=LEFT)
Label(randomoverrides, text="Overrides: ").pack(side=LEFT)
Entry(randomoverrides, textvariable=overridesvar).pack(side=LEFT)
randomgeneratebutton = Button(random_generator, text="Generate Random Board", command=generaterandom)

randomboardsize.pack()
randomoverrides.pack()
randomgeneratebutton.pack()


# Custom Board
customboardinput = Frame(custom_generator, padx=10, pady=5)
Label(customboardinput, text="Custom Board: ").pack(side=LEFT)
customboardtext = Text(customboardinput, height=8, width=25)
customboardtext.pack(side=LEFT)
customgeneratebutton = Button(custom_generator, text="Generate Custom Board", command=generatecustom)

customboardinput.pack()
customgeneratebutton.pack()

notebook.add(balanced_generator, text="Balanced")
notebook.add(random_generator, text="Random")
notebook.add(custom_generator, text="Custom")

appicon = PhotoImage(file="assets/app_splash.png")
Label(window, image=appicon, pady=15).pack()
notebook.pack()

window.mainloop()
