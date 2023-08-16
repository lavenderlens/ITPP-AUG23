# from modules.funcs_mod_2 import simple_func as simple_from_below
from funcs_mod_3 import simple_func as simple_from_above
import funcs_mod_3
import sys
sys.path.append('../ITPP-AUG23')
# imports need to come after sys
# formatter not allowing this - see VM code


# print(simple_func())
# print(simple_from_below())
# ImportError: attempted relative import with no known parent package
print(simple_from_above())
