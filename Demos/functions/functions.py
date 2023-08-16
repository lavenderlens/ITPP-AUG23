# a function is a group of one or more statements (LOC)
# which can be invoked/called one or more times at a later date
# how small cana function be?
#  one line
#  how big should a function be?
# as a rule of thumb over 50 lines or thereabouts
#  and the function is more likely to have external dependencies
# functions should ideally do one thing
#  functions may be composed of smaller functions to enable this
# so a function of say 70 lines is a candidate for other smaller functions

# functions should be idempotent
#  for the same input, they always give the same output

my_name = 'Alan'


def greet():
    print("Hello " + my_name)


greet()

my_name = "Louis"
greet()  # this is an example of an impure function that is not idempotent

# to make the above function pure, is very simple.


def greet_pure(name):
    print("Hello " + name)


greet_pure("Louis")
greet_pure("Louis")
greet_pure("Louis")
# still pure: if no change to global var, output is the same
greet_pure(my_name)
# passes in a copy

# there are FOUR main types of function
# they can have
# input
# output
# none
# or both
# input is passed in via the params
# output is yielded via the return statement
# if a function has a return, its output may be persisted or passed to another function

# candidate statements for a function?
print("Hello")
print("World")
print("How are you")

# 1. no input, no output


def greet():
    print("Hello")
    print("World")
    print("How are you")


print("greet output")

greet()

greet_output = greet()
print(greet_output)  # None
print(greet())  # no output

# 2. no input, with output (return statement)
# rules of return:
# a function or any one path through a function can only only have one return statement
# anything in a branch but under the return statement is unreachable code
# a return statement returns one value only
# that value may be a complex expression but still one thing


def greet2():
    return "Hello \nWorld \nHow are you"


greet2()  # no output

print("greet2 output")
greet2_output = greet2()
print(greet2_output)  # works
print(greet2())  # works

# 3. input AND output


def greet3(name) -> str:
    return f'Hello \n{name} \nHow are you'


print("greet3 output")
print(greet3("Alan"))

# 4. no input, output


def greet4():
    print(f'Hello \nWorld \nHow are you')


print("greet4 output")
greet4()  # NameError: name 'greet4' is not defined. Did you mean: 'greet'?


# def greet4():
#     print(f'Hello \nWorld \nHow are you')

# local variable scope

my_global = "today"


def function_1():
    my_local = "Louis"
    global my_global
    # global my_global # UnboundLocalError: cannot access local variable 'my_global' where it is not associated with a value
    print(my_global)
    my_global = 'tomorrow'
    return f'How are you {my_local} {my_global}'


def function_2():
    my_local = "Cameron"
    return f'How are you {my_local} {my_global}'


print(function_1())  # How are you Louis tomorrow
print(function_2())  # How are you Cameron tomorrow - changed also
