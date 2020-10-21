#test
#Adventure version 2 makes it so if you pick an invalid option, it does not exit like version 1 does
#Adventure version 3 adds a second set of choices if you choose the correct
def adventurev1():
    answer = input("There is a fork in the road, go left or right?")
    if answer == "left":
        print("You were eaten by an alligator.")
    elif answer == "right":
        print("You found a cake and ate it.")
    else:
        print("Please say left or right")
def adventurev2():
    cont = False
    while cont == False:
        answer = input("There is a fork in the road, go left or right?")
        if answer == "left":
            print("You were eaten by an alligator.")
            cont = True
        elif answer == "right":
            print("You found a cake and ate it.")
            cont = True
        else:
            print("Please say left or right")
def adventurev3():
    cont = False
    while cont == False:
        answer = input("There is a fork in the road, go left or right?")
        if answer == "left":
            print("You were eaten by an alligator.")
            cont = True
        elif answer == "right":
            while cont == False:
                answer = input("There's another set of paths ahead. Take the middle left or right?")
                if answer == "left":
                    print("There's a cat! You pet it and head back.")
                    cont = False
                elif answer == "middle":
                    print("There's a dog! You pet it and head back.")
                    cont = False
                elif answer == "right":
                    print("You were eaten by a Lion")
                    cont = True
                else:
                    print("Please say left, right, or middle.")
        else:
            print("Please say left or right")
            cont = False
option = ""
while option != "exit":
    option = input("Pick an adventure version (1, 2, 3). Or say exit: ")
    #  run the appropriate function based on the option the user chooses
    if option == "1":
        adventurev1()
    elif option == "2":
        adventurev2()
    elif option == "3":
        adventurev3()
    elif option == "exit":
        print("Thanks for playing!")
        # since option is now "exit", the while loop will exit.
    else:
        print("Please pick 1, 2, or 3.")

