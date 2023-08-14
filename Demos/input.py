print("Hello World")

my_name = input("please enter your name")

print(my_name)
print("Name:", my_name)
print("Name: " + my_name)

my_age = input("please enter your age: ")

print(my_age)
print("Name:", my_name, "Age:", my_age)
print("Name: " + my_name + " Age: " + my_age)

print(my_age)
# print("Name:", my_name, "Age in ten years:", my_age + 10)
# print("Name: " + my_name + " Age in ten years: " + my_age + 10)
# TypeError: can only concatenate str (not "int") to str

# find out what datatypes are by type() operator
print(type(10))  # <class 'int'>
print(type(my_age))  # <class 'str'>

my_age = int(my_age)  # conversion str --> int

print(type(my_age))  # <class 'int'> - coerced

# print("Name:", my_name, "Age in ten years:", my_age + 10)
# print("Name: " + my_name + " Age in ten years: " + my_age + 10)
# TypeError: can only concatenate str (not "int") to str

print("Name:", my_name, "Age in ten years:",
      str(my_age + 10))  # conversion int --> str
print("Name: " + my_name + " Age in ten years: " +
      str(my_age + 10))  # conversion int --> str

# way I would do it:
