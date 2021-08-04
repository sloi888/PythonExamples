VIPList = ["Randon", "Christian", "Emine", "Marzan"]
blacklist = ["Abraham", "Polina", "Ignatius"]

guest = input("What's your name? ")

if guest in VIPList:
    print("Go right on in")
elif guest in blacklist:
    print("I'm calling the cops")
else:
    print("You're not on the list")

