def intInput(prompt):
    while True:
        try:
            i = int(input(prompt))
            break
        except:
            print("Please enter an integer.")
    return i


age = intInput("Please enter your age: ")
if age >= 18:
    print("adult")
elif age > 12 and age < 18:
    print("teen")
else:
    print("child")