def printSum(num1, num2):
    print(num1 + num2)
def printProduct(num1, num2):
    print(num1 * num2)
option = True
while option:
    print("Enter the first number: ")
    num1 = int(input())
    print("Enter the second number: ")
    num2 = int(input())
    print("Enter 1 for sum or 2 for product: ")
    operation = int(input())
    if operation == 1:
        printSum(num1, num2)
    elif operation == 2:
        printProduct(num1, num2)
    else:
        print("Invalid operation")

    choice = int(input("Enter 1 to continue or 2 to quit: "))
    if choice == 2:
        option = False
