# examples made during class
end = False
while end == False:
    answer = input("Pick a number")
    if answer == "1":
        print("You were eaten by an alligator.")
        end = True
    elif answer == "2":
        print("You found a cake and ate it.")
    elif answer == "3":
        print("There were some cats")
    elif answer == "4":
        print("There were some dogs")
    elif answer == "5":
        print("There was a pineapple")
    else:
        print("Please pick a door 1-5")
print("We're outside the loop")

number = int(input("Give me a number "))

if number >= 1:
    print("it's bigger than 1")
if number >= 2:
    print("it's bigger than 2")
if number >= 3:
    print("it's bigger than 3")