Scanner keyboard = new Scanner(System.in);
System.out.println("Enter your age: ");
int age = keyboard.nextInt();
if(age < 18) { 
    System.out.println("You are a minor");
} else if(age < 65) {
    System.out.println("You are of working age");
} else {
    System.out.println("You are eligible for retirement");
}