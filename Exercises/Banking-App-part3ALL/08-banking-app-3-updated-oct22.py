class Account:
    number = 1001
    def __init__(self, name):
        self.name = name
        self.number = Account.number 
        Account.number += 1
        self.balance = 0
        print(str(self.number) + " created")

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount: 
            self.balance -= amount
        else:
            print(f'insufficient funds: balance = {self.balance}')

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def create_account(self, name): 
        self.accounts.append(Account(name)) 

    def find(self, name):
        for acc in self.accounts:
            print(acc.name)
            if not (acc.name == name):
                # print(str(acc.number) + " retrieved")
                # return acc
                return None
            # else: 
            print(str(acc.number) + " retrieved")
            return acc

myBank = Bank("My Bank")
print(id(myBank))

session = True
while(session):
    print("Enter c for create account, s for search accounts by name, or x to quit: ")
    bank_option = input()
    if bank_option == 'c':
        print("Create account: ")
        name = input()
        myBank.create_account(name) 

    elif bank_option == 's':
        name = input('search for an account name:')
        account = myBank.find(name)
        if not account == None:
            print(f'found account {account.name}')
        account_option = 0
        amount = 0
        while account_option is not 3:
            print("Enter 0 for balance enquiry, 1 for deposit, 2 for withdraw, or 3 to return to main menu: ")
            account_option = int(input())
            if account_option == 0:
                print(f'Your balance: {account.balance}\nAccount: {account.name}')

            elif account_option == 1:
                print("Enter the amount to deposit: ")
                amount = float(input())
                account.deposit(amount)
                print(f'New balance: {account.balance}')

            elif account_option == 2:
                print("Enter the amount to withdraw: ")
                amount = float(input())
                account.withdraw(amount)
            print(f'Balance remaining: {account.balance}')

    elif bank_option == 'x' or bank_option == 'X':
        session = False
        print('your session has ended')
        break
