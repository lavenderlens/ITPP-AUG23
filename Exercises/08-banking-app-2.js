class Account {
    constructor(name, number) {
        this.name = name;
        this.number = number;
        this.balance = 0;
    }
    deposit(amount) {
        this.balance += amount;
    }
    withdraw(amount) {
        if(this.balance >= amount) {
            this.balance -= amount;
        }
    }
}
var name = prompt("Enter the account name: ");
var number = prompt("Enter the account number: ");
var account = new Account(name, number);
var option = 0;
var amount = 0;
while(option != 3) {
    option = prompt("Enter 1 for deposit, 2 for withdraw, or 3 to quit: ");
    if(option == 1) {
        amount = prompt("Enter the amount to deposit: ");
        account.deposit(parseFloat(amount));
    } else if(option == 2) {
        amount = prompt("Enter the amount to withdraw: ");
        account.withdraw(parseFloat(amount));
    }
    console.log("The balance is: " + account.balance);
}