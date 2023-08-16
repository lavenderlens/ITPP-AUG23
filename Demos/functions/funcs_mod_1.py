def add(a, b):
    """Returns the sum of a and b.

    Args:
        a (float or int): The first number to add.
        b (_type_): The second number to add.

    Returns:
        float or int: a + b
    """
    # doctrings must be first line in a function
    # they should use whole sentences, correctly punctuated and sentence cased.
    return a + b


def div(a, b):
    if b > 0:
        return a / b
    return None


def div_default(a, b=1):
    if b > 0:
        return a / b
    return None

# variable no. of args - in an arbitrary sequence, un-named values


def add_many(a, b=0, *args):
    return a + b + sum(args)


# print(add_many(1, 2))
# print(add_many(1, 2, 3, 4))  # more than two args handled by *args
# # less than two args error: TypeError: add_many() missing 1 required positional argument: 'b'
# print(add_many(1))


def add_many_no_pos(*args):
    return sum(args)


# print(add_many_no_pos(1, 2, 3))
# print(add_many_no_pos())

# variable no. of args - in an arbitrary sequence, NAMED values


def add_details(name, age, **kwargs):
    details_dict = {'name': name, 'age': age}
    details_dict.update(kwargs)
    return details_dict
