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
