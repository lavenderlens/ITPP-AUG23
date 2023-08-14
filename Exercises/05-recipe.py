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