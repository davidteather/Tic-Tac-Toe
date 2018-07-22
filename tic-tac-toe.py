from tkinter import *
from tkinter import messagebox
import tkinter as tk
import random, sys, time

window = tk.Tk()
window.title("Tic-Tac-Toe")

square = [1, 2, 3, 4, 5, 6, 7, 8, 9]

tile0 = StringVar()
tile1 = StringVar()
tile2 = StringVar()
tile3 = StringVar()
tile4 = StringVar()
tile5 = StringVar()
tile6 = StringVar()
tile7 = StringVar()
tile8 = StringVar()
msg = StringVar()
msg.set("Chose a square!")

def AskReplay(mess):

    replay = tk.messagebox.askyesno(str(mess), "Would you like to play again?", icon='question')
    if replay == True:
        return 1
    elif replay == False:
        time.sleep(0.5)
        sys.exit()
        return 0
    else:
        print ("There's no way you could have gotten this error, sorry.")


def check_win(squareList):
    # Checks if there is a win on the board
    # Tiles that must be filled by one person to win
    winconditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [2, 4, 6], [0, 4, 8]]
    for a in winconditions:
        if squareList[a[0]] == "X" and squareList[a[1]] == "X" and squareList[a[2]] == "X":
            msg.set("You have won!")
            return 1
        elif squareList[a[0]] == "O" and squareList[a[1]] == "O" and squareList[a[2]] == "O":
            msg.set("The bot has won!")
            return 2
        elif (squareList[0] != 1 and squareList[1] != 2 and squareList[2] != 3 and squareList[3] != 4
              and squareList[4] != 5 and squareList[5] != 6 and squareList[6] != 7
              and squareList[7] != 8 and squareList[8] != 9):
            # Checks if tie
            msg.set("The game is a draw!")
            return 3
    else:
        return 0


def bot_place(squareList):
    # Function to deal with the bot AI
    # Bot Move suggestions ex: [0, 1, 2] means if tiles 0 and 1 are filled then the bot will go place at tile 2
    moveAI = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [2, 1, 0], [5, 4, 3], [8, 7, 6], [0, 3, 6], [1, 4, 7],
               [2, 5, 8], [8, 5, 2], [7, 4, 1], [6, 3, 0], [2, 4, 6], [0, 4, 8], [8, 4, 0], [6, 4, 2],
              [0, 6, 3], [1, 7, 4], [2, 8, 5], [0, 2, 1], [3, 5, 4], [6, 8, 7], [0, 8, 4], [2, 6, 4]]
    for a in moveAI:
        if len(a) == 3:
            if squareList[a[0]] == "O" and squareList[a[1]] == "O" and squareList[a[2]] != "X" \
                    and squareList[a[2]] != "O":
                place = a[2]
                return place
    # Different loop to 100% of the time favor the bot win
    # As before in one loop it was favoring bot win for each move suggestion
    for a in moveAI:
        if len(a) == 3:
            if squareList[a[0]] == "X" and squareList[a[1]] == "X" and squareList[a[2]] != "X" \
                    and squareList[a[2]] != "O":
                place = a[2]
                return place
    else:
        # If no sequence is matched calls the bot random function
        place = bot_random(squareList)
        return place


def bot_random(squareList):
    # bot random tile number returns tile number
    while True:
        place = random.randint(0, 8)
        if squareList[place] != "X" and squareList[place] != "O":
            return place
        else:
            continue


def usrPlace(event, arg, squareList):
    # Ensures the tile the user clicked is open
    if squareList[arg] != "X" and squareList[arg] != "O":
        # Sets clicked tile to the player
        squareList[arg] = "X"
        updateBoard(squareList)
        iswin = check_win(squareList)
        if iswin == 0:
            # If there is no win call the bot place function
            place = bot_place(squareList)
            squareList[place] = "O"
            iswin = check_win(squareList)
            updateBoard(squareList)
        if iswin != 0:
            if AskReplay("The Game is Over!") == 1:
                global square
                square = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                time.sleep(1)
                msg.set("Chose a square!")
                updateBoard(square)
            else:
                print("You really shouldn't have gotten here.")
    else:
        msg.set("That tile is already taken.")

        
def updateBoard(squareList):
    tile0.set(str(squareList[0]))
    tile1.set(str(squareList[1]))
    tile2.set(str(squareList[2]))
    tile3.set(str(squareList[3]))
    tile4.set(str(squareList[4]))
    tile5.set(str(squareList[5]))
    tile6.set(str(squareList[6]))
    tile7.set(str(squareList[7]))
    tile8.set(str(squareList[8]))


# Updates board values before the labels are drawn
updateBoard(square)
Label(textvariable=msg, font=("Helvetica", 20)).grid(column=1, row=0, padx=15, pady=15)

t0 = Label(textvariable=tile0, font=("Helvetica", 40))
t0.bind("<Button-1>", lambda event, arg=0: usrPlace(event, arg, square))
t0.grid(column=0, row=1, padx=15, pady=15)

t1 = Label(textvariable=tile1, font=("Helvetica", 40))
t1.bind("<Button-1>", lambda event, arg=1: usrPlace(event, arg, square))
t1.grid(column=1, row=1, padx=15, pady=15)

t2 = Label(textvariable=tile2, font=("Helvetica", 40))
t2.bind("<Button-1>", lambda event, arg=2: usrPlace(event, arg, square))
t2.grid(column=2, row=1, padx=15, pady=15)

t3 = Label(textvariable=tile3, font=("Helvetica", 40))
t3.bind("<Button-1>", lambda event, arg=3: usrPlace(event, arg, square))
t3.grid(column=0, row=2, padx=15, pady=15)

t4 = Label(textvariable=tile4, font=("Helvetica", 40))
t4.bind("<Button-1>", lambda event, arg=4: usrPlace(event, arg, square))
t4.grid(column=1, row=2, padx=15, pady=15)

t5 = Label(textvariable=tile5, font=("Helvetica", 40))
t5.bind("<Button-1>", lambda event, arg=5: usrPlace(event, arg, square))
t5.grid(column=2, row=2, padx=15, pady=15)

t6 = Label(textvariable=tile6, font=("Helvetica", 40))
t6.bind("<Button-1>", lambda event, arg=6: usrPlace(event, arg, square))
t6.grid(column=0, row=3, padx=15, pady=15)

t7 = Label(textvariable=tile7, font=("Helvetica", 40))
t7.bind("<Button-1>", lambda event, arg=7: usrPlace(event, arg, square))
t7.grid(column=1, row=3, padx=15, pady=15)

t8 = Label(textvariable=tile8, font=("Helvetica", 40))
t8.bind("<Button-1>", lambda event, arg=8: usrPlace(event, arg, square))
t8.grid(column=2, row=3, padx=15, pady=15)


window.mainloop()

