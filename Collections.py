list1 = [1,2,3,4]
tuple1 = (4,5,6) # tuples cannot be changed, only replaced
list1[1] = 8
print(list1)
tuple1 = (4,8,6)
print(tuple1)

# dictionaries use key value pairs
bank = {"Mike": 1000000, "Andre": 27358902758903, "Chris": 1000}
print(bank["Mike"])
print(bank["Andre"])
millionaires = []
for person in bank:
    if bank[person] >= 1000000:
        millionaires.append(person)
print(millionaires)

