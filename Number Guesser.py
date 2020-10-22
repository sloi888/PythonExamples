import random
min = 1
max = 20
number = random.randint(min, max)
tryAgain = True
while tryAgain is True:
    guessesLeft = 5
    correct = False
    attempts = 0
    while guessesLeft > 0 and correct is False:
        while True:
            try:
                guess = int(input(f"The number is between {min} and {max}. You have {guessesLeft} guesses left."))
                break
            except:
                print("Please type an integer.")
        attempts += 1
        guessesLeft -= 1
        if guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low!")
        else:
            correct = True
            print(f"Correct! It took you {attempts} tries")

    if correct is False:
        print(f"Sorry, the number was {number}")
    response = input("Try again? (y/n)").lower()
    if response == "y" or response == "yes":
        tryAgain = True
    else:
        tryAgain = False