# determine if a string is an address or not
# an address is a set of numbers, followed by a set of characters
# followed by a 2 character suffix (st, rd, etc.)

# get the address
# split the address into pieces wherever there's a space, turning it into a list

def addressSplit(address:str):
    splitAddress = address.split(" ")
    streetNumber = splitAddress[0]
    street = ''
    # start with an empty string, append each piece of the street name to it
    # with a space as well so it's properly formatted
    for item in splitAddress[1:-1]:
        street += item + " "
    # then chop off the extra empty space
    street = street[:-1]
    # the suffix is the last thing in the string we gave
    suffix = splitAddress[-1]
    # check if the first part is only numbers
    acceptableSuffixes = ["st", "rd", "cir", "ave", "blv", "plc"]
    isNumberOK = streetNumber.isnumeric()
    isSuffixOK = suffix in acceptableSuffixes
    if isNumberOK:
        print("The first part is a number")
    else:
        print("The first part must be a number")
    # check if the third part is 2 characters
    if isSuffixOK:
        print("suffix OK")
    else:
        print("Please use an acceptable suffix")
    return [streetNumber, street, suffix]


while True:
    addr = input("Please enter an address")
    if addr == "exit" or addr == "quit":
        break
    result = addressSplit(addr)
    print(result)
