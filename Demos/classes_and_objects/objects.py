# see objects_intro.txt

# Python does not have an object literal as such (object created without using a class) but has dicts
alan = {"name": "Alan", "Age": 21, "Instruments": ["trombone", "keys", "vox"]}

tom = {"firstName": "Tom", "lastName": "Morello",
       "age": 65, "instruments": "guitar"}

band = [alan, tom]

# for member in band:
#     print(member["firstName"]) #KeyError - with no uniform prop names

# what we need is a system for giving our objects the same attributes from the start
# this doesn't mean they all have same values


class Musician:
    # constructor
    def __init__(self, name, age, instruments):
        self.name = name
        self.age = age
        self.instruments = instruments
    # dunder methods (double underscore) str

    def main_instrument(self):
        return f'{self.name}\'s main instrument is {self.instruments[0]}'

    def __str__(self):
        return f'Musician {self.name} is {self.age} years old and plays {self.instruments}'


alan2 = Musician("Alan", 21, ["trombone", "keys", "vox"])
tom2 = Musician("Tom Morello", 65, ["guitar"])

# object properties referenced by dot notation
# NOT square brackets as in dictionaries!
print(alan2.instruments)  # ['trombone', 'keys', 'vox']
print(tom2.age)  # 65

# print dictionaries:
# {'name': 'Alan', 'Age': 21, 'Instruments': ['trombone', 'keys', 'vox']}
print(alan)
# {'firstName': 'Tom', 'lastName': 'Morello', 'age': 65, 'instruments': 'guitar'}
print(tom)

# print objects:
print(alan2)  # <__main__.Musician object at 0x102e8e7d0>
print(tom2)  # <__main__.Musician object at 0x102e8e810>

# with NO CHANGE to runtime code
# the dunder method __str__ is implemented and results are:
# Musician Alan is 21 years old and plays ['trombone', 'keys', 'vox']
# Musician Tom Morello is 65 years old and plays ['guitar']

# using class method:
print(alan2.main_instrument())
print(tom2.main_instrument())

alan3 = alan2  # shallow copy
print(alan3 == alan2)  # True #NOTE:
# this behaviour is ofetn not the case in other languages

# pass by references / pass by value / pass by copies
# case 1: values (immutable variables)
#   number value
x = 1


def changeIt(number):
    number += 1


changeIt(x)
print(x)  # ?1 - value not changed - a COPY of it is passed to the function


def changeItGlobal():
    global x
    x += 1


changeItGlobal()  # nothing passed in - impure function
print(x)  # 2


# case 2: references (mutable objects)

def changeItObj(musician):
    musician.name = "Bruce Springsteen"


changeItObj(alan2)
print(alan2)  # references work differently - any changes have to be visible across all references to same object
