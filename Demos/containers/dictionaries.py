# a dictionary (Python dict type) is a mutable, unordered container of key value pairs
# keys MUST be unique and, ideally, immutable
# values may be duplicated
# both values and keys, crucially, may be of mixed datatypes
# dictionaries are therefore a way of encapsulating different data in one place
# dicts are commonly used to represent complex data
# they enforce a tightly-coupled relationships between each key and its value

# creation
book = {}  # note that this will be of type dict NOT set!
book2 = dict()
print(type(book))  # <class 'dict'>
print(type(book2))  # <class 'dict'>

# adding and updating
# we set props on the dict and pass them values
book['title'] = 'The First Casualty'  # adds new key value pair
book['title'] = 'Post Mortem'  # updates key value pair
book['author'] = "Ben Elton"
book["pub_year"] = 1995

# getting a value
title = book['title']
print(title)

# dict objects have various methods
pub_year = book.pop('pub_year')
# this REMOVEs that prop
# print(book['pub_year']) # KeyError: 'pub_year'

# iterating
for key in book:
    print(key)

# you could hack the keys to return the values
for key in book:
    print(book[key])

# but this is a special method to return keys only
for value in book.values():
    print(value)

for key, value in book.items():
    print(key, value)
