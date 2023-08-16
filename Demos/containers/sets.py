# a set is a mutable, unordered container that DOES NOT permit duplcates
#  sets are commonly used to strip duplicates from lists

# creation
unique_nums1 = {3, 3, 3, 10, 10, 2, 2}
unique_nums2 = set([3, 3, 3, 10, 10, 2, 2])

# from dictionaries file, we see that empty {} is type dict
# to make an empty set use constructor above
empty_set1 = {}
print(type(empty_set1))  # <class 'dict'>
empty_set2 = set()
print(type(empty_set2))

print(unique_nums1)  # {1, 2, 3} # {3, 2, 10}
print(unique_nums2)  # {1, 2, 3} # {2, 10, 3}

# we can convert sets back into lists
list_of_unique_nums = list(unique_nums2)
print(list_of_unique_nums)  # [2, 10, 3]

# some set methods are very powerful fro transforming/inspecting data:

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}  # 3 and 4 are in both sets
set3 = set1.intersection(set2)
print(set3)  # {3, 4} - reflexive, non-associative, order does not matter
set4 = set1.difference(set2)
print(set4)  # {1, 2} - associative, order matters
set5 = set2.difference(set1)
print(set5)  # {5,6} - associative, order matters
set6 = set1.symmetric_difference(set2)
print(set6)  # {1, 2, 5, 6}
set7 = set2.symmetric_difference(set1)
print(set7)  # {1, 2, 5, 6} - reflexive, non-associative - order doesn't matter
