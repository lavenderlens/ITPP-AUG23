var magicNumber = parseInt((Math.random() * 10) + 1);
var numGuess = 1;
var win = false;
while(numGuess <= 3) {
    var userGuessString = prompt("Guess the magic number in the range 1-10. Guess " + numGuess + " of 3: ");
    // var userGuess = parseInt(userGuessString);
    if(userGuess == magicNumber) {
        console.log("You got it!");
        win = true;
        break;
    } else if(userGuess + 1 == magicNumber || userGuess - 1 == magicNumber) {
        console.log("So close!");
    } else {
        console.log("Way off!");
    }
    numGuess += 1;
}
if(win) {
    console.log("You win!");
} else {
    console.log("You lose!");
}