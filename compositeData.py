class Animal:
    def __init__(self):
        self.name = ''
        self.age = 0
        self.colors = []
        self.sex = ''
        self.species = ''

    def describe(self):
        print(f"{self.name} is a {self.sex} {self.colors} {self.species} that is {str(self.age)} years old.")


Kiwi = Animal()
Kiwi.name = "Kiwi"
Kiwi.age = 3
Kiwi.colors = ['Brown', 'Black']
Kiwi.sex = "female"
Kiwi.species = "cat"

Kiwi.describe()

KiwiDict = {
    'name': "Kiwi",
    'age': 3,
    'colors': ['Brown', 'Black'],
    'sex': 'female',
    'species': 'cat'
}

print(KiwiDict)
