month = input('enter the name of the month: ')
if month.lower() == 'february':
    print("No.of days is 28")
elif month.lower() == 'september' or month == 'april' or month == 'june' or month == 'november':
    print("No.of days is 30")
else:
    print("No.of days is 31")

# Thirty days hath September,
# April, June, and November,
# All the rest have thirty-one,
# Except February, twenty-eight days clear,
# And twenty-nine in each leap year.

# Your task is to code up a program that will
# 1. take a month from the User
# 2. tell the user how many days are in that month
# 3. don't worry about leap years - February has 28 days.