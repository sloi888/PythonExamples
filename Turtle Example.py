# turtle documentation: https://docs.python.org/3/library/turtle.html

import turtle

t = turtle.Turtle()

def turtleStar(size):
    for i in range(5):
        t.forward(size)
        t.right(144)

def askInput():
    # Keep asking for input until they give us valid input
    # we exit the function when we return some value, which will only happen when the input is validated.
    while True:
        print("What should the turtle do?: ")
        # Ask for user input, change it to all lowercase, and split wherever there's a space, leaving us with a list
        # of the words or numbers that the user entered
        userInput = input().lower().split()
        # limit them to only 2 words, a command and an argument
        if len(userInput) > 2:
            print("Too many arguments. Please type a command and a number")
        else:
            # if they only say exit, provide a blank argument and return the pair
            if len(userInput) == 1:
                return (userInput[0], "")
            # otherwise save the first element of their input as the command and the second as the argument
            else:
                # we need to try to convert the argument from a string to a float.
                # if we don't, we will get an error if we try something like t.forward("apple") down the line
                try:
                    return (userInput[0], float(userInput[1]))
                # this happens if the above 'try' block fails
                # meaning they put an argument that could not be converted properly to a float.
                # if we don't do this and they enter something that can't be converted, the program will crash
                except:
                    print("Please enter a number after the command.")


# call the appropriate function based on the user's command, using the argument that they gave us as well
def doCommand(command, argument):
    if command == "exit" or command == "quit":
        exit()
    elif command == "left" or command == "l":
        t.left(int(argument))
    elif command == "right" or command == "r":
        t.right(int(argument))
    elif command == "forward" or command == "f":
        t.forward(int(argument))
    elif command == "star" or command == "s":
        turtleStar(int(argument))
    else:
        print("Please say 'forward', 'left', 'right', or 'star' in addition to a number. Or say 'exit' to quit.")


def welcome():
    print("""Welcome to the interactive turtle program!
    Please give the turtle instructions
    You can tell the turtle to move forward, turn left or right, or draw a star of a certain size
    For example, you can say 'forward 15'
    'left 90' or 'star 50'""")


welcome()
# repeat the input -> command loop until they quit
while True:
    userInput = askInput()
    # pass the command and argument we got to the doCommand function
    doCommand(userInput[0], userInput[1])