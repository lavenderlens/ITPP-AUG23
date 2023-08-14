# EXTENSION EXERCISE
# It's all well to say n squared is n * n
# but what of n cubed? n * n * n?
# and n to the power of 8?
# to raise something to the power of n in Python is **
# where the first operand is the number and the second the power

# 1. refactor your code to accept an exponent (power)
# then loop through, as before, 
# calculating different values against the exponent, 
# as long as the user doesn't type a zero to quit

# 2. refactor your code further so that the program does not accept just one exponent to raise the number to
# but as many different ones as you like, implementing the existing loop for each exponent
# and allowing your user to do as many as they want,
# then go back and change the value of the exponent
# and do a bunch of calculations again, as many as they want, based on the new exponent value

# when they finally quit the whole thing, print "goodbye" to the console
# hint: to facilitate this, two loops are necessary
# don't go mad: expect to solve in under 20 LOC

proceed1 = True

while(proceed1):
    exponent = int(input("MAIN MENU:\nenter the exponent (power) you wish to calculate \n(eg. cubed, the exponent is 3)\nEnter a zero (0) to quit\n"))
    if exponent == 0:
        proceed1 = False
    else:
        proceed2 = True
        while(proceed2):
            print(f'''Enter a number to raise to the power {exponent}, 
            or 0 to return to main menu:
            ''')
            number = int(input())
            if number == 0:
                proceed2 = False
            else:
                print(number ** exponent)
print('goodbye')


    

