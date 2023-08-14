var name = prompt("Enter the name: ");
var age = prompt("Enter the age: ");
var isValid = age >= 18 && age <= 125;
console.log("The age, " + age + " of " + name + " is valid: " + isValid);

// with template literal:

console.log(`${ name }'s age ${ age } 
is valid: ${ isValid }`);