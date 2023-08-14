dayOfWeek = 7
age = 64

if dayOfWeek == 6:
    print("Saturady!")
elif dayOfWeek == 7:
    print("Sunday")
else:
    print("its a weekday")

if age < 18:
    print("you are a minor")
else:
    if age < 65:
        print("you are working age")
    else:
        print("You are eligible for retiremnt")
        print("non-indented block")
