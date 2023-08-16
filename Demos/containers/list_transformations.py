# in functional programming, or FP, we seek to produce or extract new information from old
# the original information is treated as if it were immutable

# here we backwards-engineer three popular list transformations
# by doing this we see the workings explicitly

# the goal of these transformations is to extract new information from old
#  without changing the original


band = ["Bruce", "Patti", "Max", "Gary", "Soozie", "Stevie",
        "Nils", "Tom", "Clarence", "Jake", "Danny", "Roy"]

# 1.
# using a Python for loop, iterate over the band list
# each member whose name is shorter than 5 characters
# should be added to a new list called short_names
# this is the equivalent of a filter function and returns a new list
# with SOME of the original elements that passa test (predicate function)
# the original is unchanged
# this is a choice or style rather than syntax
# i.e. we could mutate the original, but choose not to

short_names = []

for member in band:
    if len(member) < 5:  # the predicate
        short_names.append(member)
print(short_names)

# 2.
# using the band list, output a new list called starred
# with "**E-Street " prpended to each member name
# and "**" appended to each name
# print out the new listthis is the equivalent of a map function and returns a new list
# with each/every element transformed

starred = []

for member in band:
    starred.append(f'**E-Street {member}**')

# print(starred)
for member in starred:
    print(member)

# 3.
# from band, output a single string
# with each member comma-separated
# this is the equivalent of a reducer function
# and returns a single value from an input list

sentence = ''

for member in band:
    sentence += f'{member},'

print(sentence)

# 4. as a challenge,
# output the same as above 4.
# but with a full stop at the end of the sentence
# revisit after loops section
# it requires a loop that has knowledge of idx

sentence = ''
# have to use while loop to access index!
counter = 0
while counter < len(band):
    if counter == len(band) - 1:
        sentence += f'{band[counter]}.'
        # counter += 1
    else:
        sentence += f'{band[counter]}, '
        # counter += 1
    counter += 1

print(sentence)
