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
var smith = new Account("Smith", 12345);
smith.deposit(100);
console.log(smith.balance);
smith.withdraw(75);
console.log(smith.balance);
smith.withdraw(50);
console.log(smith.balance);