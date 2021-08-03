list1 = [1,2,3,4]
tuple1 = (4,5,6)  # tuples cannot be changed, only replaced
list1[1] = 8
print(list1)
list1.append(5)
print(list1)
tuple1 = (4,8,6)
print(tuple1)

# dictionaries use key value pairs


def applyInterest(accounts):
    print("Applying interest")
    for account in accounts:
        print(f"{account} had ${accounts[account]} in it")
        accounts[account] = accounts[account] * 1.01
        print(f"After applying interest {account} has ${accounts[account]} in it")


bank = {"Mike": 1000000, "Andre": 27358902758903, "Chris": 1000}
# print(bank["Mike"])
# print(bank["Andre"])
millionaires = []
print(bank)
applyInterest(bank)
print(bank)
applyInterest(bank)
print(bank)
applyInterest(bank)

for person in bank:
    if bank[person] >= 1000000:
        millionaires.append(person)


print(millionaires)

