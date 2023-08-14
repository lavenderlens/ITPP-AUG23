print("Enter your age: ")
age = int(input())
if age < 18:
    print("You are a minor")
elif age < 65:
    print("You are of working age")
else:
    print("You are eligible for retirement")
