var proceed = true;
while(proceed) {
    var number = prompt("Enter a number to square, or 0 to quit: ");
    if(number == 0) {
        proceed = false;
    } else {
        console.log(number * number);
    }
}