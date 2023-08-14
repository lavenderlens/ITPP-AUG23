class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age



def changeIt(number):
    number += 1
    #return number
x =1
#x = changeIt(x)
changeIt(x)
print(x)
# a copy of x is passed into the function

def changeIt2(person):
    person.name = "Paul"

saul = Person("Saul",30)
changeIt2(saul)
print(saul.name)

#dictionary example, from docs https://docs.python.org/3/tutorial/datastructures.html
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
# gallahad the pure
# robin the brave
for k, v in knights.items():
    print(k)
for k, v in knights.items():
    print(v)

#escaping quotes
print("Lavender was amazed at Jones' audacity")
print('Lavender was amazed at Jones\' audacity')
print('Lavender was "amazed" at Jones\' audacity')
print("Lavender was \"amazed\" at Jones\' audacity")