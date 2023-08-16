# a tuple is an immutable, indexed (oredred) container that permits duplicate elements
# you are unlikely to use tuples directly!

# they are a perfect for, say, reading in data from database table rows

def get_stats(a_list_of_numbers) -> tuple:
    min_num = min(a_list_of_numbers)
    max_num = max(a_list_of_numbers)
    sum_nums = sum(a_list_of_numbers)
    # each value here is wrapped in a tuple automatically
    print(type(max_num))  # <class 'int'>
    return min_num, max_num, sum_nums


# run the function and elements in the tuple are automatically unwrapped
mn, mx, sm = get_stats([1, 2, 3, 4])
print(mn, mx, sm)
print(type(mn))  # <class 'int'>

get_stats_tuple = get_stats([1, 2, 3, 4])
print(get_stats_tuple)  # (1, 4, 10)
print(type(get_stats_tuple))  # <class 'tuple'>
