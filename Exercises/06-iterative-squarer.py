proceed = True
while(proceed):
    print("Enter a number to square, or 0 to quit: ")
    number = int(input())
    if number == 0:
        proceed = False
    else:
        print(number * number)
