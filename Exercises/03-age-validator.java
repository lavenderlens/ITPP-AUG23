Scanner keyboard = new Scanner(System.in);
System.out.println("Enter the age: ");
int age = keyboard.nextInt();
boolean isValid = age >= 18 && age <= 125;
System.out.println("The age is valid: " + isValid);