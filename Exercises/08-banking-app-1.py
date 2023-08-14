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
smith = Account("Smith", 12345)
smith.deposit(100)
print(smith.balance)
smith.withdraw(75)
print(smith.balance)
smith.withdraw(50)
print(smith.balance)