def getAverage(numbers):
    # sum = 0
    # count = 0
    # average
    # for number in numbers:
    #     sum += number
        # count += 1
    # average = sum / count
    # return average
    # return sum / count
    # return sum / len(numbers) # length is always implicitly known 
    return sum(numbers) / len(numbers)#using builtin sum()!

# >>> dir (__builtins__)[dir(__builtins__).index('abs'):]

housePrices = [318000, 347000, 428000, 282000, 273000, 362000, 343000, 332000]
averageHousePrice = getAverage(housePrices)
print("Average house price: " + str(averageHousePrice))
print(getAverage([23, 95, 41, 66, 38]))