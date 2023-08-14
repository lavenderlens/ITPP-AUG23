ingredients = ["chicken", "breadcrumbs", "salt", "garlic", "lime"]
print("ORIGINAL")
print(ingredients[0])
print(ingredients[1])
print(ingredients[2])
print(ingredients[3])
print(ingredients[4])
ingredients[4] = "lemon"
ingredients.append("rocket")
del ingredients[2]
print("AFTER CHANGES")
print(ingredients[0])
print(ingredients[1])
print(ingredients[2])
print(ingredients[3])
print(ingredients[4])

directions = ['chop', 'coat in', 'add', 'crush', 'sprinkle']
print(f'{directions[0]} {ingredients[0]}')
print(f'{directions[1]} {ingredients[1]}')
print(f'{directions[2]} {ingredients[2]}')
print(f'{directions[3]} {ingredients[3]}')
print(f'{directions[4]} {ingredients[4]}')

# initialise another array (technically speaking a list in Python) called directions
# with directions for each ingredient, in the same order as the ingredients
# sample data:
# ingredients[4] is "lemon"
# directions[4] should read "sprinkle" or something appropriate
# 
# ingredients[0] is "chicken"
# directions[0] should read "chop" or something appropriate
# 
# print out the relevant elements from BOTH arrays
# sample output should be 
# "chop chicken"
# "dip in breadcrumbs"
# and so on