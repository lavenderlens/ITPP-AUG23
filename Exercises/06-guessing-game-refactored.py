import random
magicNumber = random.randint(1, 10)
print('pssst hint: the number is ', magicNumber)
numGuess = 1
win = False
while numGuess <= 3 and win == False:
    print("Guess the magic number in the range 1-10. Guess " + str(numGuess) + " of 3: ")
    userGuess = int(input())
    if userGuess == magicNumber:
        print("You got it!")
        win = True
        # numGuess = 4 # same as setting this
    elif userGuess + 1 == magicNumber or userGuess - 1 == magicNumber:
        print("So close!")
    else:
        print("Way off!")
    numGuess += 1
if win:
    print("You won!")
else:
    print("You lose!")
