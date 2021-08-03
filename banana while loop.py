bananas = 5
while bananas > 0:
    if bananas >= 5:
        print("large bunch")
    elif 1 <= bananas <= 4:
        print("small bunch")
    elif 0 > bananas:
        print("You're in banana debt")
    else:
        print("no bananas")
    print("You ate a banana")
    bananas -= 1
    # bananas = bananas - 1
    print(f"You have {bananas} bananas left")