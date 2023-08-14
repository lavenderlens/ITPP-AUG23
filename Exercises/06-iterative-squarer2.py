proceed = True
while(proceed):
    number = int(input("Enter a number to square, or 0 to quit: "))
    if number == 0:
        proceed = False
    else:
        print(number * number)
