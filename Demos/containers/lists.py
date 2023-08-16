#  a list is a mutable, indexed (ordered) container that permits duplicates
#  lists are commonly used to store groups of objects of the same tyope
#  note technically everything in Python is an object

# creation
nums = [1, 2, 3]  # initialised with values
nums2 = list()  # empty list constructor

print(nums)
print(nums2)

nums2.append(3)
nums2.append(4)
nums2.append(5)
print(nums2)

# indexing
first_num = nums[0]  # read - non-mutating
nums[1] = 22  # write - mutating
print(nums)

# creating a new list that is a subset of another
fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print(len(fib))

# use square brackets but with arguments, colon-separated
# from idx 3 to the end
slice1 = fib[3:]
print(slice1)

# from idx (inclusive) to end idx (exclusive)
slice2 = fib[3:9]
print(slice2)  # [2, 3, 5, 8, 13, 21] - misses last value
slice3 = fib[3:10]
print(slice3)
# note there isn't a 11th element
# print(fib[10]) # IndexError: list index out of range

# step (3rd argument colon-separated)
slice4 = fib[4:10:2]
print(slice4)
slice5 = fib[::2]
print(slice5)  # [0, 1, 3, 8, 21] - whole list, step of 2

# counting back from end
slice6 = fib[::-2]
print(slice6)  # [34, 13, 5, 2, 1]

# remove / delete
del fib[0]  # operator - variable after operator
print(fib)
fib.remove(1)  # function - called ON variable
print(fib)  # removes first instance [1, 2, 3, 5, 8, 13, 21, 34]

# delete when idx not known
del fib[fib.index(8)]
print('# delete when idx not known')
print(fib)
# insert at index
# fib.insert(4, 8)
fib.insert(fib.index(13), 8)
print(fib)

# append
fib.append(55)
print(fib)

# iterating (brief)
# the Python for loop looks like the JS for-of loop or the Java enhanced for loop
# it has no explicit knowledge of index position
for num in fib:
    print(num)

# some builtins for lists
num_elements = len(fib)
sum_elements = sum(fib)
min_element = min(fib)
max_element = max(fib)

print(num_elements, sum_elements, min_element, max_element)

# arithmetic operations
# add two lists
new_list = fib + nums
print(new_list)

multiplied_list = nums * 10
print(multiplied_list)  # NOT each element multiplied by ten
# the three elements in nums, repeated ten times
