float getAverage(int[] numbers) {
    int sum = 0;
    // int count = 0;
    for(int number : numbers) {
        sum += number;
        // count += 1;
    }
    // return sum / count;
    return sum / numbers.length;

}
int[] housePrices = {318000, 347000, 428000, 282000, 273000, 362000, 343000, 332000};
float averageHousePrice = getAverage(housePrices);
System.out.println("Average house price: " + averageHousePrice);
//added
int[] numbers1 = {23, 95, 41, 66,38};
		System.out.println(getAverage(numbers1));