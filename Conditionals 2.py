# if elif else

# if checks a condition, executes the code within it if the condition is true

# elif (optional) checks additional conditions, if the initial if statement did not execute

# else (optional) catches any other case

name = input("Tell me your name: ").lower()

if len(name) > 10:
    print("I can't remember that, it's too long")
    if name[0] == "c":
        print("Hey my name also starts with C")
if name == "mike":
    print("Hey I know a bunch of Mikes")
if "x" in name:
    print("wow your name has an X in it, that's wild")
print("nice to meet you")

# if len(name) > 10:
#     print("I can't remember that, it's too long")
# elif name[0] == "c":
#     print("Hey my name also starts with C")
# elif name == "mike":
#     print("Hey I know a bunch of Mikes")
# elif "x" in name:
#     print("wow your name has an X in it, that's wild")
# else:
#     print("nice to meet you")