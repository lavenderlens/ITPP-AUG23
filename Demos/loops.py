# loops are repetitive program structures that either
# 1. loop around elements of a collection until the end is reached
# 2. loop to a counter until the counter has finished
# 3. loop indefinitely (infinite loop) until some other condition changes (usually via user I/O)
# while loops are generally used for types 2 and 3
# for loops are generally used for looping round containers
# there are other data structures more suited for lookups eg Dictionaries

# 3.
# while True:
#     # loop code here
#     name = input('Enter your name: ')
#     if len(name):  # if a name is entered it ahs a length
#         print(f'you entered {name}')
#         break  # terminate infinite loop
#         # often called the happy (not sad)
#     else:
#         print('You did not enter anything!')

# 2.
num_greetings = 0
while num_greetings < 3:
    print('Hello')
    num_greetings += 1  # DANGER -
    # when using a counter,
    # if you omit this you will get an infinite loop

# 1.
# looping round a list
names = ["Louis", "Cameron", "Alan"]
for name in names:
    print(name)

#  looping round a dict
coords = {'x': 12, 'y': 3, 'z': 0}
for key in coords:
    print(f'{key} : {coords[key]}')

# looping round a string
word = 'chocolate'
for char in word:
    print(char)

# the Python range function is sometimes used for looping around acounter
# in this case below the output is a range of numbers 0-9
for num in range(10):
    print(num + 1)

# unique in Python: and optional else may be added to a loop

# file reading:
with open('python_context.txt') as file:
    # for line in file:
    #     # print(line)
    #     # print(line.strip())
    #     if line.startswith('ERROR'):
    #         print('the file has an error')
    #         break
    #     else:
    #         print(line.strip())
    #         print('File processed - no errors')
    lines = list(file)
    print(lines)
    for line in lines:
        if line.startswith('ERROR'):
            print(f'error found on line {lines.index(line) + 1}')
