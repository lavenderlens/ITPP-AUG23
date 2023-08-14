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
Scanner keyboard = new Scanner(System.in);
System.out.println("Enter the account name: ");
String name = keyboard.nextLine();
System.out.println("Enter the account number: ");
int number = keyboard.nextInt();
Account account = new Account(name, number);
int option = 0;
int amount = 0;
while(option != 3) {
    System.out.println("Enter 1 for deposit, 2 for withdraw, or 3 to quit: ");
    option = keyboard.nextInt();
    if(option == 1) {
        System.out.println("Enter the amount to deposit: ");
        amount = keyboard.nextInt();
        account.deposit(amount);
    } else if(option == 2) {
        System.out.println("Enter the amount to withdraw: ");
        amount = keyboard.nextInt();
        account.withdraw(amount);
    }
    System.out.println("The balance is: " + account.balance);
}