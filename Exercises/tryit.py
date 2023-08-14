# myList = [1,2,3,4]
# myList.append(5)
# print(myList)
# myList2 = ["1","2","3","4"]
# myList.append('')
# print(myList)
# del myList2[1]
# print(myList2)
# print(len(myList2))

# for x in range(1,6):
#   print(x)


# def greet(name, age):
# 	yearOfBirth = 2017 - age
# 	print("Hello " + name)
# 	print("You were born in " + str(yearOfBirth))

# greet("Al",33)


#08
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def sayHello(self):
		print("Hello, my name is " + self.name)
# me = Person("Big Al",33)
#careful of the indents on the repl - best run from file

def changeIt(number):
	number += 1
x = 1
changeIt(x)
print(x)

def changeItObj(person):
	person.name = "Paul"
saul = Person("Saul", 30)
changeItObj(saul)
print(saul.name)
saulCopy = saul
saulCopy.name = 'The Apostle Paul'
print(saulCopy.name)
print(saul.name)# two refs point to same obj




