var age = prompt("Enter your age: ");
if(age < 18) {
    console.log("You are a minor");
} else if(age < 65) {
    console.log("You are of working age");
} else {
    console.log("You are eligible for retirement");
}

//manual requirements changed to leave out if-else
var isValid = age >= 18 && age <=125;

console.log('input age: ' + age + ', valid? ' + isValid);