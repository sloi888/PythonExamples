# arrays are defined with []
array = ["a", "b", "c"]

# tuples are defined with ()
tuple = ("d", "e", "f")

# dictionaries are defined with {}
dictionary = {
    "name" : "Stephen",
    "class" : "AWS"
}

for item in array:
    print(item)
for item in tuple:
    print(item)
for key, value in dictionary.items():
    print(key,value)
