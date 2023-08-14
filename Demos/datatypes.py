my_floating_point_num = 2.5
my_whole_num = 2

print(type(my_floating_point_num))  # <class 'float'>
print(type(my_whole_num))  # <class 'int'>

# often called DUCK-TYPING
# Python is a dynamically-typed language
# takes its type from the data
# can be changed / coerced

my_whole_num = float(my_whole_num)
print(my_whole_num)  # 2.0 - no data loss
# example of an upcast - smaller type into bigger one

my_floating_point_num = int(my_floating_point_num)
print(my_floating_point_num)  # 2 - data loss
# example of an downcast - bigger type into smaller one

my_bool = True
print(type(my_bool))

my_str = "hello"  # <class 'bool'>
print(type(my_str))  # <class 'str'>

# constants - variables whose value may not be chanegd
# no inherent support in Python
# but container type Tuple is immutable

my_list = [1, 2, 3]
my_list[0] = 99
print(my_list)

my_tuple = (1, 2, 3)
# my_tuple[0] = 99 # TypeError: 'tuple' object does not support item assignment

#  as we see, tuples are a form of constants
