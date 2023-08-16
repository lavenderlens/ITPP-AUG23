class Account:
    # number = 1001
    def __init__(self,name,number):
    # def __init__(self, name):
        self.name = name 
        self.number = number 
        # self.number = Account.number 
        # Account.number += 1
        self.balance = 0 
  
    def deposit (self, amount):
        self.balance += amount
        print("Balance for account:%s is %.2f" %(self.name, self.balance) ) 
  
    def withdraw (self,amount):
        if (self.balance - amount >= 0):
            self.balance -= amount
            print("Balance for account:%s is %.2f" %(self.name, self.balance) ) 
        else:
            print("Not enough funds for this withdrawal") 

class Bank:

    def __init__(self, name ):
        self.name = name 
        self.accounts = []

    def openAccount(self, name, number):
       if self.getAccount(number) == None: 
           account = Account(name,number)
           self.accounts.append(account)
           print("Created account - name:" , name, " number:", number)
       else:
           print("The account number:", number, "is already assigned, try another!")
       

    def getAccount(self,number):
        for account in self.accounts:
            if account.number == number:
                return account 
        return None

    def closeAccount(self,number):
        for idx in range(len(self.accounts)):
            if self.accounts[idx].number == number:
               self.accounts.pop(idx)
               print("Successfully removed account" , number)

firstdirect = Bank("First Direct")

while ( True ):
    option = input("Enter option: 1 to create account, 2 to deposit, 3 to withdraw, 4 to close account, 5 to quit: ") 
    try:
        option = int(option)
    except ValueError:
        print('Non-numeric value entered, returning to the main menu')
        continue

    if option not in [1,2,3,4,5]:
        print("Invalid option, please try again")
        continue

    elif ( option == 5 ):
       print("Exiting Application")
       break

    number = input("Enter account number: ")
    if not number.isdigit():
        print('Non-numeric value entered, account creation aborted')
        continue
    elif firstdirect.getAccount(number): # Account number already exists
        print(f'account number {number} already assigned, account creation aborted')
        continue


    if ( option == 1): 
            name = input("Enter account name: ")
            if not name.isalpha():
                print('Account name must be alpha characters only, account creation aborted!')
                continue

    elif ( option in [2,3,4,5] ):
            account = firstdirect.getAccount(number)
            if account == None:
                print("Account number not recognised, try again")
            elif (option == 2):
                amount = input("Enter amount to deposit: ") 
                try:
                    amount = float(amount) 
                    account.deposit(amount)
                except ValueError:
                    print('Non-numeric value entered, deposit transaction aborted')

            elif ( option == 3 ):
                amount = input("Enter amount to withdraw: ") 
                try:
                    amount = float(amount) 
                    account.withdraw(amount)
                except ValueError:
                    print('Non-numeric value entered, withdrawal transaction aborted')

            else:
                firstdirect.closeAccount(number)
