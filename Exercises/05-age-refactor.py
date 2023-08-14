age = int(input('what is you age?'))
if age > 0 and age < 18:
	print('too young to work')
elif age > 65 and age < 125:
	print('past retirement age')
elif age >= 18 and age <= 65:
	print('working age')
else:
    print('invalid age')