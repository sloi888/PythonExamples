# turtle documentation: https://docs.python.org/3/library/turtle.html

import turtle

t = turtle.Turtle()

def turtleStar(size):
    for i in range(5):
        t.forward(size)
        t.right(144)

def askInput():
    while True:
        userInput = input().lower().split()
        if len(userInput) > 2:
            print("Too many arguments. Please type a command and a number")
        else:
            if len(userInput) == 1:
                command = userInput[0]
            else:
                command = userInput[0]
                argument = userInput[1]
        if command == "left":
            t.left(int(argument))
        elif command == "right":
            t.right(int(argument))
        elif command == "forward":
            t.forward(int(argument))
        elif command == "star":
            turtleStar(int(argument))
        elif command == "exit" or command == "quit":
            exit()
        else:
            print("Please say 'forward', 'left', 'right', or 'star' in addition to a number.")
def welcome():
    print("""Welcome to the interactive turtle program!
    Please give the turtle instructions
    You can tell the turtle to move forward, turn left or right, or draw a star of a certain size
    For example, you can say 'forward 15'
    'left 90' or 'star 50'""")
# print(t.position())
# t.speed(20)
# for i in range(180):
#     t.forward(.5)
#     t.right(1)
# print(t.position())
welcome()
askInput()