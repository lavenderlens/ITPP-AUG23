# a string is an immutable, indexed (ordered) container of characters that permits duplicates

s1 = "Hello"
s2 = "Hello"
s3 = str("Hello")

# are these considered to be equal as they have the same characters in the same order?

print(s1 == s2 == s3)  # True
print(s1.__eq__(s2))  # True
print(s1.__eq__(s3))  # True

# NOTE: this doesn't compare to JS or Java

# escape characters are escaped with a \
#  common ones (apart from r): \' \" \n \r \t \\
quote = 'he said "I think therefore I am"'  # cheat or hack using double/single
quote = "he said \"I think therefore I am\""  # cheat or hack using double/single

# triple quotes have two main uses
# to preserve line breaks in code
sql_query = '''
select * from books_table
where title = ?
and author = ?
'''
# in docstrings, see functions section

# concatenation (joining together) of strings
#  old school python 2
heading_text = 'My Website'
old_school = '<h1>' + heading_text + "</h1>"

#  new python 3.5>
new_concat = f'<h1>{heading_text}</h1>'

# string objects have many buil-in methods
# most are transformative - they return a new string based on the existing with transformation applied

s = 'Hello World'
print(s.lower())
print(s)

# we may re-assign the original reference variable (s) to the new transformed value
s = s.upper()
print(s)
# but this re-assignment of reference variable
# does not destroy the original string from memory
# but simply de-refeences it
