import random
magicNumber = random.randint(1, 10)
userGuess = int(input("Guess the magic number in the range 1-10: "))
if userGuess == magicNumber:
    print("You got it!")
elif userGuess + 1 == magicNumber or userGuess - 1 == magicNumber:
    print("So close!")
else:
    print("Way off!")
# print('Magic Number was ' + str(magicNumber))
# print("It was {}".format(magicNumber))
# print(f'It was: \n{ magicNumber }')
print(f'''
It was:
{ magicNumber }
''')
