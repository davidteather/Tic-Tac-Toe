import os, time, random, sys
print("Python Tic-Tac-Toe" + os.linesep)
print("GitHub: https://github.com/davidteather/Tic-Tac-Toe" + os.linesep)


def printBoard(squareList):
    # Function Prints the board
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


def check_win(squareList):
    # Checks if there is a win on the board
    # Tiles that must be filled by one person to win
    winconditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [2, 4, 6], [0, 4, 8]]
    for a in winconditions:
        if len(a) == 3:
            if squareList[a[0]] == "X" and squareList[a[1]] == "X" and squareList[a[2]] == "X":
                return 1
            elif squareList[a[0]] == "O" and squareList[a[1]] == "O" and squareList[a[2]] == "O":
                return 2
            elif (squareList[0] != 1 and squareList[1] != 2 and squareList[2] != 3 and squareList[3] != 4
                  and squareList[4] != 5 and squareList[5] != 6 and squareList[6] != 7
                  and squareList[7] != 8 and squareList[8] != 9):
                print(" " + os.linesep)
                print(squareList[0])
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


def usr_placeinput(squareList):
    # Deals with user placement and because of sloppy code everything else
    while True:
        try:
            # Asks for tile input
            place = int(input("Where would you want to place your X?" + os.linesep))
            # Verifies that the tile exists
            if 0 < place < 10:
                # Subtracts one from input because indexing starts at 0 not 1
                place -= 1
                # Checks if there is any tiles already placed there
                if squareList[place] != "X" and squareList[place] != "O":
                    squareList[place] = "X"
                    # Calls check_win and returns value
                    iswin = check_win(squareList)
                    if iswin == 0:
                        bval = bot_place(squareList)
                        squareList[bval] = "O"
                    iswin = check_win(squareList)
                    printBoard(squareList)
                    # Deals with what the check_win function returns
                    if iswin == 1:
                        print("You have won!" + os.linesep)
                    elif iswin == 2:
                        print("The Bot has won!" + os.linesep)
                    elif iswin == 3:
                        print("You have managed to tie against... a bot. Good Job!")
                    if iswin != 0:
                        # Asks if user would like to play again
                        val = input("Would you like to play again y | n" + os.linesep).lower()
                        if val == "y":
                            print("Resetting..." + os.linesep)
                            time.sleep(1.5)
                            # Resets list to original value and reprints board
                            squareList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                            # Loops back to beginning of the game
                            printBoard(squareList)
                            continue
                        elif val == "n":
                            # If user doesn't want to play again exit
                            print("Good Bye.")
                            time.sleep(.5)
                            print("Exiting...")
                            time.sleep(1.5)
                            sys.exit()
                        else:
                            # If not a valid input resets anyways because yeah.
                            print("Not a valid input")
                            time.sleep(.5)
                            print("Resetting Anyways...")
                            time.sleep(1)
                            squareList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                            printBoard(squareList)
                            continue
                elif squareList[place] == "X" or squareList[place] == "O":
                    # Says the place is already taken
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


# Sets the tiles to be equal to begin with
squares = [1, 2, 3, 4, 5, 6, 7, 8, 9]
while True:
    # Starts the game
    printBoard(squares)
    placement = usr_placeinput(squares)

