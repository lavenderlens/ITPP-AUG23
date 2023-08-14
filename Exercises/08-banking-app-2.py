class Account:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
print("Enter the account name: ")
name = input()
print("Enter the account number: ")
number = int(input())
account = Account(name, number)
option = 0
amount = 0
while option != 3:
    print("Enter 1 for deposit, 2 for withdraw, or 3 to quit: ")
    option = int(input())
    if option == 1:
        print("Enter the amount to deposit: ")
        amount = float(input())
        account.deposit(amount)
    elif option == 2:
        print("Enter the amount to withdraw: ")
        amount = float(input())
        account.withdraw(amount)
    #print("The balance is: " + str(account.balance))
    print("The balance is: {}".format(account.balance))
