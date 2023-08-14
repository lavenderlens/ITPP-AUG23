function printSum(num1, num2) {
    console.log(parseInt(num1) + parseInt(num2));
}
function printProduct(num1, num2) {
    console.log(parseInt(num1) * parseInt(num2));
}
while(true) {
    var num1 = prompt("Enter the first number: ");
    var num2 = prompt("Enter the second number: ");
    var operation = prompt("Enter 1 for sum or 2 for product: ");
    if(operation == 1) {
        printSum(num1, num2);
    } else if(operation == 2) {
        printProduct(num1, num2);
    } else {
        console.log("Invalid operation");
    }
    var option = prompt("Enter 1 to continue or 2 to quit: ");
    if(option == 2) {
        break;
    }
}