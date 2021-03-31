# requirements
# X's & O's / Players
# board
# turns
# rules
# win condition

# process
import random
spaces = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
# board = \
#     f" {spaces[0]} | {spaces[1]} | {spaces[2]} \n"\
#     "-----------\n" \
#     f" {spaces[3]} | {spaces[4]} | {spaces[5]} \n" \
#     "-----------\n" \
#     f" {spaces[6]} | {spaces[7]} | {spaces[8]} \n"


def updateBoard():
    global board
    board = \
        f" {spaces[0]} | {spaces[1]} | {spaces[2]} \n" \
        "-----------\n" \
        f" {spaces[3]} | {spaces[4]} | {spaces[5]} \n" \
        "-----------\n" \
        f" {spaces[6]} | {spaces[7]} | {spaces[8]} \n"


def printBoard(spc):
    b = \
        f" {spc[0]} | {spc[1]} | {spc[2]} \n" \
        "-----------\n" \
        f" {spc[3]} | {spc[4]} | {spc[5]} \n" \
        "-----------\n" \
        f" {spc[6]} | {spc[7]} | {spc[8]} \n"
    print(b)


def makeMove(player):
    # while they are still giving us an invalid number, keep them here
    # ensure that their move is valid
    # valid means:
    # 1. Empty spot
    # 2. Inside the board
    # 3. Is an integer
    isChoiceValid = False
    while isChoiceValid == False:
        try:
            desiredNum = input("Enter number: ")
            num = int(desiredNum)
            if num >= 0 and num <= 8:
                if spaces[num].isnumeric():
                    isChoiceValid = True
                else:
                    print("That space is occupied, you fool")
            else:
                print("That's outside the board")
        except:
            print("Hey that wasn't a integer, you fool")
    # using num, update a space on the board with the current player's symbol
    spaces[num] = player
    printBoard(spaces)


def isThereAWinner(spc):
    # game is over when 1 player has 3 in a row, or all spaces are full
    possibleWins = [[0, 1, 2], # horizontal wins
                    [3, 4, 5],
                    [6, 7, 8],
                    [0, 3, 6], # vertical wins
                    [1, 4, 7],
                    [2, 5, 8],
                    [0, 4, 8], # diagonal wins
                    [2, 4, 6]]
    # check if players have 3 in a row
    for wincombo in possibleWins:
        if spc[wincombo[0]] == spc[wincombo[1]] == spc[wincombo[2]]:
            return True
    return False


def isItADraw(spc):
    if spc.count("X") == 4 and spc.count("O") == 5:
        return True
    elif spc.count("X") == 5 and spc.count("O") == 4:
        return True
    else:
        return False


printBoard(spaces)
# decide who goes first
players = ["X", "O"]
goingFirst = random.choice(players)
currentPlayer = goingFirst
print(f"{goingFirst} is first")


while True:
    # first player decides where to go
    print(f"It is {currentPlayer}'s turn")
    makeMove(currentPlayer)
    if isThereAWinner(spaces):
        print(f"{currentPlayer} wins!")
        break
    elif isItADraw(spaces):
        print("No one wins")
        break
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

