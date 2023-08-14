// console.log(sum, count);//ERROR

function getAverage(numbers) {
    var sum = 0; // local to function 
    // var count = 0; // local to function
    // initialising to zero not only sets value to 0 but TYPE TO NUMBER
    for(number of numbers) {
        sum += number;
        // count += 1;
    }
    // return sum / count;
    return sum / numbers.length;
}
var housePrices = [318000, 347000, 428000, 282000, 273000, 362000, 343000, 332000];
var averageHousePrice = getAverage(housePrices);
console.log("Average house price: " + averageHousePrice);
console.log(getAverage([23, 95, 41, 66, 38]));