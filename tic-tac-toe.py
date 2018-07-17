import os
import time
import random
import sys
print("Python Tic-Tac-Toe" + os.linesep)
print("GitHub: https://github.com/davidteather/Tic-Tac-Toe" + os.linesep)


def printBoard(squareList):

    str(squareList)
    print("     |     |     ")
    print("  " + str(squareList[0]) + "  |  " + str(squareList[1]) + "  |  " + str(squareList[2]) + "  ")
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print("  " + str(squareList[3]) + "  |  " + str(squareList[4]) + "  |  " + str(squareList[5]) + "  ")
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print("  " + str(squareList[6]) + "  |  " + str(squareList[7]) + "  |  " + str(squareList[8]) + "  ")
    print("     |     |     " + os.linesep)


def usr_placeinput(squareList):
    while True:
        try:
            place = int(input("Where would you want to place your X?" + os.linesep))
            if 0 < place < 10:
                place -= 1
                if squareList[place] != "X" and squareList[place] != "O":
                    squareList[place] = "X"
                    iswin = check_win(squareList)
                    if iswin == 0:
                        bval = bot_place(squareList)
                        squareList[bval] = "O"
                    iswin = check_win(squareList)
                    printBoard(squareList)
                    if iswin == 1:
                        print("You have won!" + os.linesep)
                    elif iswin == 2:
                        print("The Bot has won!" + os.linesep)
                    elif iswin == 3:
                        print("You have managed to tie against... a bot. Good Job!")
                    if iswin != 0:
                        val = input("Would you like to play again y | n" + os.linesep).lower()
                        if val == "y":
                            squareList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                            printBoard(squareList)
                            continue
                        elif val == "n":
                            print("Good Bye.")
                            time.sleep(3)
                        else:
                            print("Not a valid input")
                            sys.exit() # change to be decent
                elif squareList[place] == "X" or squareList[place] == "O":
                    print("That place is already taken." + os.linesep)
                    printBoard(squares)
                    continue
            else:
                print("That is not a valid tile." + os.linesep + "If you believe this is an error make an issue report on https://github.com/davidteather/Tic-Tac-Toe" + os.linesep)
                continue
        except ValueError:
            print("That is not a valid integer." + os.linesep + "If you believe this is an error make an issue report on https://github.com/davidteather/Tic-Tac-Toe" + os.linesep)
            continue
        else:
            continue


def bot_place(squareList):
    while True:
        place = random.randint(0,8)
        if squareList[place] != "X" and squareList[place] != "O":
            return place
        else:
            continue


def check_win(squareList):
    if (squareList[0] == "X" and squareList[1] == "X" and squareList[2] == "X" or
            squareList[3] == "X" and squareList[4] == "X" and squareList[5] == "X" or
            squareList[6] == "X" and squareList[7] == "X" and squareList[8] == "X" or
            squareList[0] == "X" and squareList[3] == "X" and squareList[6] == "X" or
            squareList[1] == "X" and squareList[4] == "X" and squareList[7] == "X" or
            squareList[2] == "X" and squareList[5] == "X" and squareList[8] == "X" or
            squareList[0] == "X" and squareList[4] == "X" and squareList[8] == "X" or
            squareList[6] == "X" and squareList[4] == "X" and squareList[2] == "X"):
        print(" " + os.linesep)
        return 1
    elif (squareList[0] == "O" and squareList[1] == "O" and squareList[2] == "O" or
            squareList[3] == "O" and squareList[4] == "O" and squareList[5] == "O" or
            squareList[6] == "O" and squareList[7] == "O" and squareList[8] == "O" or
            squareList[0] == "O" and squareList[3] == "O" and squareList[6] == "O" or
            squareList[1] == "O" and squareList[4] == "O" and squareList[7] == "O" or
            squareList[2] == "O" and squareList[5] == "O" and squareList[8] == "O" or
            squareList[0] == "O" and squareList[4] == "O" and squareList[8] == "O" or
            squareList[6] == "O" and squareList[4] == "O" and squareList[2] == "O"):
        print(" " + os.linesep)
        return 2
    elif (
        squareList[0] != 1 and squareList[1] != 2 and squareList[2] != 3 and
        squareList[3] != 4 and squareList[4] != 5 and squareList[5] != 6 and
        squareList[6] != 7 and squareList[7] != 8 and squareList[8] != 9
    ):
        print(" " + os.linesep)
        print(squareList[0])
        return 3
    else:
        return 0


squares = [1, 2, 3, 4, 5, 6, 7, 8, 9]
while True:
    printBoard(squares)
    placement = usr_placeinput(squares)

