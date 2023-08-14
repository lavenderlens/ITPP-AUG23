def printSum(num1, num2):
    print(num1 + num2)

def printProduct(num1, num2):
    print(num1 * num2)

while True:
    print("Enter the first number: ")
    num1 = int(input())
    print("Enter the second number: ")
    num2 = int(input())
    # print("Enter 1 for sum or 2 for product: ")
    # operation = int(input())
    operation = input("Enter 1 for sum or 2 for product: ")
    if operation == '1':
        printSum(num1, num2)#printSum is not defined - if def code is after runtime
    elif operation == '2':
        printProduct(num1, num2)
    else:
        print("Invalid operation")
    print("Enter 1 to continue or 2 to quit: ")
    option = int(input())
    if option == 2:
        break

# def printSum(num1, num2):
#     print(num1 + num2)

# def printProduct(num1, num2):
#     print(num1 * num2)
