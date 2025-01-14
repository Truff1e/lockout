from tkinter import *
from lockout import *
from index import exclusiveSets
from generator import parse_options
from tkinter import ttk
import os


def boardoutputwindow(board, gentype: str):
    outputwindow = Tk()
    outputwindow.title("Generated Board")
    outputwindow.geometry("300x250+300+300")
    outputwindow.resizable(False, True)

    goal_list = Text(outputwindow)

    if gentype == 'balanced':
        goal_list.insert('end', "BALANCED BOARD\n\n")
        goal_list.insert('end', f"Board Size: {int(sizevar.get()//1)**2} \n")
        goal_list.insert('end', f"Difficulty: {difficultyvar.get().__round__(1)} \n")
        goal_list.insert('end', f"Blackout Mode: {blackoutvar.get()} \n")
        goal_list.insert('end', "Excluded Goals: \n")
        for goal in goal_checkboxes_list:
            if not goal_checkboxes_list[goal].get():
                goal_list.insert('end', f"{goal}, ")
    elif gentype == 'custom':
        goal_list.insert('end', "CUSTOM BOARD\n")
    goal_list.insert('end', "\n\nBoard Goals: ")
    for goal in board:
        goal_list.insert('end', f"\n{goal} - {goalDictionary[goal][0]}")
    goal_list.insert('end', "\n\nGoal List: ")
    for goal in board:
        goal_list.insert('end', f"{goal},")
    goal_list.config(state=DISABLED)
    goal_list.pack()
    outputwindow.mainloop()

def generatebalanced():
    if blackoutvar.get():
        excluded = []
        for goal in goal_checkboxes_list:
            if not goal_checkboxes_list[goal].get():
                excluded.append(goal)
        for goal in exclusiveSets['opponent']:
            excluded.append(goal)
        print("Generating Blackout Board")
    else:
        excluded = []
        for goal in goal_checkboxes_list:
            if not goal_checkboxes_list[goal].get():
                excluded.append(goal)
        print("Generating Lockout Board")
    print(excluded)
    board = balancedboard(int(sizevar.get()//1)**2, str(difficultyvar.get().__round__(1)).split(','), excluded=excluded)
    boardoutputwindow(board, 'balanced')

def generatecustom():
    customboard(customboardtext.get("1.0", "end-1c").strip(" ").split(','))
    boardoutputwindow(customboardtext.get("1.0", "end-1c").strip(" ").split(','), 'custom')

def getsizesildervalue():
    return int(sizevar.get()//1)

def getdifficultysildervalue():
    return '{: .1f}'.format(difficultyvar.get())

def randomgoal():
    goal = getrandomgoal()
    return f"{goal} - {goalDictionary[goal][0]}"


# Window
window = Tk()
window.title("Lockout Generator")
window.geometry("350x300+150+150")
window.resizable(False, False)

# window.iconphoto(True, PhotoImage(file='./assets/logo1024.png'))

# Notebook Windows
notebook = ttk.Notebook(window)

balanced_window = ttk.Frame(window)
custom_window = ttk.Frame(window)
goal_window = ttk.Frame(window)
settings_window = ttk.Frame(window)


# Variables
sizevar = DoubleVar()
sizevar.set(5)
blackoutvar = BooleanVar()
blackoutvar.set(False)
difficultyvar = DoubleVar()
difficultyvar.set(4)
overridesvar = StringVar()
customgoallistvar = StringVar()
translatevar = StringVar()
goalidvar = StringVar()
output_path_var = StringVar()


# Balanced Board
boardsize = ttk.Frame(balanced_window, padding=5)
difficulty = ttk.Frame(balanced_window, padding=5)
overrides = ttk.Frame(balanced_window, padding=5)

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
blackouttoggle = ttk.Checkbutton(balanced_window, text="Blackout Mode", variable=blackoutvar, padding=10)
generatebutton = ttk.Button(balanced_window, text="Generate Balanced Board", command=generatebalanced)

boardsize.pack()
difficulty.pack()
blackouttoggle.pack()
generatebutton.pack()


# Custom Board
customboardinput = ttk.Frame(custom_window, padding=10)
ttk.Label(customboardinput, text="Custom Board: ").pack(side=LEFT)
customboardtext = Text(customboardinput, height=7, width=25)
customboardtext.pack(side=LEFT)
customgeneratebutton = ttk.Button(custom_window, text="Generate Custom Board", command=generatecustom)

customboardinput.pack()
customgeneratebutton.pack()


goal_checkboxes_canvas = Canvas(goal_window)
goal_checkboxes_scroll = ttk.Scrollbar(goal_window, orient="vertical", command=goal_checkboxes_canvas.yview)
goal_checkboxes_canvas.config(yscrollcommand=goal_checkboxes_scroll.set)
goal_checkboxes = ttk.Frame(goal_checkboxes_canvas)

goal_checkboxes_scroll.pack(side="right", fill="y")
goal_checkboxes_canvas.pack(side="left", fill="both", expand=True)
goal_checkboxes_canvas.create_window((0, 0), window=goal_checkboxes, anchor='nw')


goal_checkboxes.bind("<Configure>", lambda e: goal_checkboxes_canvas.configure(scrollregion=goal_checkboxes_canvas.bbox("all")))

goal_checkboxes_list = {}
for i in goalDictionary:
    goal_enabled = BooleanVar()
    goal_checkboxes_list[i] = BooleanVar()
    goal_checkboxes_list[i].set(True)
    checkbutton = ttk.Checkbutton(goal_checkboxes, text=f'{i} - {goalDictionary[i][0]}', variable=goal_checkboxes_list[i])
    checkbutton.pack(anchor='w')


# Options
output_path_var = parse_options()['output_path']
output_path = ttk.Entry(settings_window, textvariable=output_path_var)
output_path.pack()

# Notebook Packing
notebook.add(balanced_window, text="Balanced")
notebook.add(custom_window, text="Custom")
notebook.add(goal_window, text="Goals")
notebook.add(settings_window, text="Options")

app_splash_ref = os.path.join(os.path.dirname(__file__), './assets/app_splash.png')

appicon = PhotoImage(file=app_splash_ref)
Label(window, image=appicon, pady=15).pack()
Label(window, text=f"v{parse_options()['version'][:-1]} - Created by Truff1e", pady=3).pack()
notebook.pack()


window.mainloop()
