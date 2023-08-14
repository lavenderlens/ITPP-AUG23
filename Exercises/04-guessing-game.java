int magicNumber = (int) (Math.random() * 10) + 1;
Scanner keyboard = new Scanner(System.in);
System.out.println("Guess the magic number in the range 1-10:");
int userGuess = keyboard.nextInt();
if(userGuess == magicNumber) {
    System.out.println("You got it!");
} else if(userGuess + 1 == magicNumber || userGuess - 1 == magicNumber) {
    System.out.println("So close!");
} else {
    System.out.println("Way off!");
}