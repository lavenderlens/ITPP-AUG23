class Account {
    String name;
    int number;
    float balance;
    Account(String name, int number) {
        this.name = name;
        this.number = number;
        this.balance = 0;
    }
    void deposit(float amount) {
        this.balance += amount;
    }
    void withdraw(float amount) {
        if(this.balance >= amount) {
            this.balance -= amount;
        }
    }
}
Account smith = new Account("Smith", 12345);
smith.deposit(100);
System.out.println(smith.balance);
smith.withdraw(75);
System.out.println(smith.balance);
smith.withdraw(50);
System.out.println(smith.balance);