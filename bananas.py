while True:
    bananas = int(input("How many bananas? "))
    if bananas >= 5:
        print("large bunch")
    elif 1 <= bananas <= 4:
        print("small bunch")
    elif 0 > bananas:
        print("You're in banana debt")
    else:
        print("no bananas")
