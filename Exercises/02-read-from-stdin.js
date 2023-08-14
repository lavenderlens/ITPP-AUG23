var name = prompt("Enter the account name: ");
var number = prompt("Enter the account number: ");
var balance = prompt("Enter the account balance: ");
var isTaxable = Boolean(prompt("Enter the taxable flag (true or false): "));

//
// if(isTaxable =='true'){
// 	isTaxable = true;
// } else if(isTaxable == 'false'){
// 	isTaxable = false;
// }

//
console.log("Name: " + name);
console.log("Number: " + number);
console.log("Balance: " + balance);
console.log("Is taxable: " + isTaxable);

if (isTaxable) {
  console.log("boolean");
}
