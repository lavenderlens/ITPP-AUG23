import funcs_mod_1  # needs qualified function names
from funcs_mod_1 import *  # wildcard import
from funcs_mod_1 import add, div, add_details  # preferred style
# because
# A) no need to qualify the function when used
# B) next person will know which one(s) out of all used

print(funcs_mod_1.add(1, 3))  # qualified name
print(add(1, 3))  # no need

# not considered best practice
# not because there is any performance overhead for linking more functions
# but because of readability -
# what functions from the module did the last developer use?

print(div(4, 2))

details = add_details("Alan", 21)
print(details)
details_2 = add_details("Alan", 21, tel="07442 173 078", address="TN24 8JX")
print(details_2)
