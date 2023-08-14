var magicNumber = parseInt((Math.random() * 10) + 1);
var userGuessString = prompt("Guess the magic number in the range 1-10: ");
var userGuess = parseInt(userGuessString);
if(userGuess == magicNumber) {
    console.log("You got it!");
} else if(userGuess + 1 == magicNumber || userGuess - 1 == magicNumber) {
    console.log("So close!");
} else {
    console.log("Way off!");
}