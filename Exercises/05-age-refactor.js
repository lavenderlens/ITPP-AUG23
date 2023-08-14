var age = prompt('what is you age?');
if(age > 0 && age < 18){
	console.log('too young to work');
} else if(age > 65 && age < 125) {
	console.log('past retirement age');
} else if (age >= 18 && age <= 65){
	console.log('working age');
} else console.log('invalid age');