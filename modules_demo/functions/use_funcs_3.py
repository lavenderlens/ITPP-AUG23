import sys
sys.path.append("../TEST")
import funcs_mod_3 # qualified
from funcs_mod_3 import func as f # aliased

funcs_mod_3.func() # qualified
f()# aliased
