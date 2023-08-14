var magicNumber = parseInt((Math.random() * 10) + 1);
var numGuess = 1;
var win = true;
do{
    var userGuessString = prompt("Guess the magic number in the range 1-10. Guess " + numGuess + " of 3: ");
    var userGuess = parseInt(userGuessString);
    
    if(userGuess + 1 == magicNumber || userGuess - 1 == magicNumber) {
        console.log("So close!");
        win = false;
    } else if(userGuess != magicNumber) {
        console.log("Way off!");
        win = false;
    }
        else {
            console.log("You got it!");

    }
    numGuess += 1;
}while(numGuess <= 3 && !win) 
if(!win) {
    console.log("You lose!");
} else {
    console.log("You win!");
}