from oo_calc import *

calc = Calculator()  # we make an instance of the class
calc.add(5)
calc.multiply(3)
calc.subtract(1)
calc.divide(2)
print(calc.equals())

calc2 = Calculator()  # new instance resets everything
calc2.add(5)
calc2.multiply(3)
calc2.subtract(1)
calc2.divide(2)
print(calc2.equals())
