def greet(name, name2):
    print("Hello", name, "and", name2)
    #print("welcome", name)

#greet("Alan")

alan = "Alan"

greet(alan, "Mike")

def greet2(name, age):
    year = 2017 - age
    print("Hello",name,"you are",year,"years old")

greet2("Alan",1966)

numbers = [1,2,3,4,5,1,2,3,4,5]

def sum(nums):
    sum = 0
    for num in nums:
        sum += num
    return sum

print(sum(numbers))

greet2("Alan",sum(numbers))

def retirable(name,age):
    isRetirable = False
    if age > 65:
        isRetirable = True
        print(name,"can retire")
        return isRetirable
    else :
        print(name,"is not yet reiring age")
        return isRetirable

retirable("Alan",33)

workers = []

if retirable("Mike", 66):
    workers.append("Mike")
else:
    print("not time to retire")

print("Workers:",workers)
