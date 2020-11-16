def initializeSpaces():
    # referring to spaces as global lets other functions access it
    # as long as they also say that they are using the global 'spaces' variable
    global spaces
    # create a list with 9 empty elements
    spaces = [''] * 9
    # same as: spaces = ['', '', '', '', '', '', '', '', '']
    for i in range(1,10):
        spaces[i-1] = str(i)
    # same as: spaces = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def updateBoard():
    # referring to board as global lets other functions access it
    # as long as they also say that they are using the global 'board' variable
    global board
    # backslashes let you make a multiline string
    board = f' {spaces[0]} | {spaces[1]} | {spaces[2]}\n' \ 
            f'-----------\n' \
            f' {spaces[3]} | {spaces[4]} | {spaces[5]}\n' \
            f'-----------\n' \
            f' {spaces[6]} | {spaces[7]} | {spaces[8]}'
    #prints as:
    #  1 | 2 | 3
    # -----------
    #  4 | 5 | 6
    # -----------
    #  7 | 8 | 9


def makeMove(player):
    # take the player as a parameter so we can use it for X and for O
    # make sure all the functions are talking about the same variables
    # by having them refer to them as global
    global spaces
    global board
    validMove = False
    # Keep asking the user for input until the move they choose is valid
    while validMove == False:
        # Make sure the player's input is an integer.
        # Catch errors from converting invalid input to an integer
        while True:
            try:
                print(board + '\n')
                move = int(input(f"{player}'s turn, make your move: ")) - 1
                break
            except:
                print("Please enter a number from 1 to 9")
        # Make sure their choice is within the board
        if move >= 0 and move <= 8:
            # Make sure their chosen spot is unoccupied
            if spaces[move] != 'X' and spaces[move] != 'O':
                # If so, set the chosen spot to the current player's mark
                spaces[move] = player
                # set validMove to True so we exit the loop
                validMove = True
                # a move is only valid if it's from 0-8 and the space is not occupied
                # this is the only way to exit the loop of asking for a move
            else:
                print("That space is already occupied")
        else:
            print("Please enter a number from 0 to 8")
    updateBoard()


def thereIsAWinner():
    global spaces
    # if 3 subsequent spaces are all the same value
    # (either X or O) then the value that occupies that space is the winner
    #  0 | 1 | 2
    # -----------
    #  3 | 4 | 5
    # -----------
    #  6 | 7 | 8
    # check horizontal spaces
    # top row
    if spaces[0] == spaces[1] == spaces[2]:
        return True
    # middle row
    elif spaces[3] == spaces[4] == spaces[5]:
        return True
    # bottom row
    elif spaces[6] == spaces[7] == spaces[8]:
        return True
    # check vertical spaces
    # left column
    elif spaces[0] == spaces[3] == spaces[6]:
        return True
    # middle column
    elif spaces[1] == spaces[4] == spaces[7]:
        return True
    # right column
    elif spaces[2] == spaces[5] == spaces[8]:
        return True
    # check diagonal spaces
    # top left to bottom right
    elif spaces[0] == spaces[4] == spaces[8]:
        return True
    # top right to bottom left
    elif spaces[2] == spaces[4] == spaces[6]:
        return True
    # otherwise there are no winners
    else:
        return False


def itIsADraw():
    global spaces
    # iterate through every space
    for space in spaces:
        # if a space isn't an X or an O, it must be a number, meaning it isn't used
        if space != "X" and space != "O":
            # so it is not a draw
            return False
    # if we make it through every space without finding an empty one
    # it means they're all full, so it's a draw
    return True


def playGame():
    # reset the spaces to numbers
    initializeSpaces()
    # update the board variable
    updateBoard()
    winner = ''
    # alternate between X and O making moves until the game is over
    while True:
        makeMove("X")
        if thereIsAWinner():
            winner = "X"
            break
        if itIsADraw():
            winner = "No one"
            break

        makeMove("O")
        if thereIsAWinner():
            winner = "O"
            break
        if itIsADraw():
            winner = "No one"
            break
    print(board + '\n')
    print(f"{winner} wins!")
    # if the game ended via turn limit, winner will still be 'No one'
    # you could make a special 'It's a draw' statement if you wanted to with an if statement


# The main program. Code starts running from here
# repeat playGame
while True:
    playGame()
    r = input("Play again? (y/n): ").lower()
    if r == "n" or r == 'no':
        break
