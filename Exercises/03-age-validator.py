# exercise age-validator
# age = int(input("Enter the age: "))
# isValid = (age >= 18) and (age <= 125)
# print('The age {} is valid: {}'.format(age, isValid))

# with three methods of placeholder string formatting:

name = input("Enter your name: ")
age = int(input("Enter your age: "))
isValid = (age >= 18)  and (age <= 125)


# 1
print(name + '\'s age is ' + str(age) + '\nValid? ' + str(isValid))
# works for Python 2

# 2 Python 3 on
print('{}\'s age is {} \nValid? {}'.format(name, age, isValid))
# variable values get computed into string representations
# placeholders must be the right number and right order

# 3 Python 3.5 on ✅
print(f'{name}\'s age is {age} \nValid? {isValid}')
# placeholders can accept inline variables


# 4 Python 3.7 on 
print(f'''
{name}\'s age is {age} 
Valid? {isValid}''') 
# very similar to JS template literals see below

