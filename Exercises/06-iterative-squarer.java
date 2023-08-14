boolean proceed = true;
Scanner keyboard = new Scanner(System.in);
while(proceed) {
    System.out.println("Enter a number to square, or 0 to quit: ");
    int number = keyboard.nextInt();
    if(number == 0) {
        proceed = false;
    } else {
        System.out.println(number * number);
    }
}