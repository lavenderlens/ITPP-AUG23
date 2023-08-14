def getAverage(numbers, label):
    total = 0
    # count = 0
    for n in numbers:
        total += n
        # count += 1
    return str(total / len(numbers)) + " for " + label
housePrices = [318000, 347000, 428000, 282000, 273000, 362000, 343000, 332000]
averageHousePrice = getAverage(housePrices, "Ashford")
print("Average house price: " + str(averageHousePrice))
print(getAverage([23, 95, 41, 66, 38], "Donegal"))
#print(getAverage("stupid", True))# different datatypes wont compile