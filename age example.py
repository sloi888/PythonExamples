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
elif age > 65:
    print("senior citizen")
elif age > 35 and age < 55:
    print("midlife crisis")
else:
    print("child")
