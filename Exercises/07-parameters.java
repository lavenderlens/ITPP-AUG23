void printSum(int num1, int num2) {
    System.out.println(num1 + num2);
}
void printProduct(num1, num2) {
    System.out.println(num1 * num2);
}
Scanner keyboard = new Scanner(System.in);
while(true) {
    System.out.println("Enter the first number: ");
    int num1 = keyboard.nextInt();
    System.out.println("Enter the second number: ");
    int num2 = keyboard.nextInt();
    System.out.println("Enter 1 for sum or 2 for product: ");
    int operation = keyboard.nextInt();
    if(operation == 1) {
        printSum(num1, num2);
    } else if(operation == 2) {
        printProduct(num1, num2);
    } else {
        System.out.println("Invalid operation");
    }
    System.out.println("Enter 1 to continue or 2 to quit: ");
    int option = keyboard.nextInt();
    if(option == 2) {
        break;
    }
}