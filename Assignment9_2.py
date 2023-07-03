from Assignment9_1 import *

op = MathOperations(5,10)

addr = op.add()
subr = op.sub()
mulr = op.mul() 

try:
    divr = op.div()
except ZeroDivisionError as z:
    print("Division Error: Cannot divide by 0",z)

powr = op.pow()
flrDvr = op.floorDiv()

