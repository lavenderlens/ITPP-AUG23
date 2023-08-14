# one branch
if False:
    print('IF block executed')

print('carrying on with rest of code...')

# the if statement is the main conditional structure
# it executes a suite of code depending on a condition
# each statement in the if block MUST be indented
# the default convention is 4 spaces / 1 tab
# the block is ended when the indentation is ended
# note that only ONE block is execited in a multi-branch if statement

#  2 branches

if False:
    print('IF block executed')
else:
    print('else block executed')
# note else block has NO condition

#  we may want to test / match more than one if condition

# 3 or more branches

if False:
    print('IF block executed')
elif True:
    print('ELIF statement executed')
else:
    print('else block executed')

# nested IF statements are possible but not necessarily easy to read
dayOfWeek = 6
if dayOfWeek >= 6:
    if dayOfWeek == 7:
        print('It is Sunday')
    else:
        print('It\'s a Saturday')
else:
    print('It\'s a weekday')

# OR, without nesting (just!)
if dayOfWeek >= 1 and dayOfWeek <= 7:
    if dayOfWeek == 6:
        print('It\'s a Saturday')
    elif dayOfWeek == 7:
        print('It is Sunday')
    else:
        print('It\'s a weekday')
else:
    print("invalid day")

#  there is no limit to the number of elif statements you can have

#  there are two additional structures in other languages:
#  the ternary operator
# the switch statement

# the ternary operator does not exist in Python as such
# but is an if else on one line
camera_flash = False
room_light = 5

if room_light > 2:
    camera_flash = False
else:
    camera_flash = True

#  OR, on one line
camera_flash = True if room_light <= 2 else False

#  Python has no equivalent of the switch statement
#  but in recent versions the match statement is introduced
#  this works similarly and is suited for
#  individual hard-coded values
# whereas if ... elif ... else is suited for RANGES

# num = 'x'
# num = 4
# num = 'y'
num = True  # tries to match True with zero value, fails, matches next case which is 1
# num = int('1')
match num:
    case 0:
        print('The number is 0')
    # case 1:
    #     print('The number is 1')
    case 2:
        print('The number is 2')
    case 'x':
        print('The number is x')
    case 3:
        print('The number is 3')
    case True:
        print("The number is True")
    case _:
        print('I don\'t know what the number is')

print("match refactored as if ... elif")
if num == 0:
    print('The number is 0')
elif num == 1:
    print('The number is 1')
elif num == 2:
    print('The number is 2')
elif num == 'x':
    print('The number is x')
elif num == 3:
    print('The number is 3')
elif num == True:
    print("The number is True")
else:
    print('I don\'t know what the number is')
