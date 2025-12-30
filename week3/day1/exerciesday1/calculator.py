
import operators
print(operators.addOperator(10,10))
print(operators.divideOperator(10,10))

from operators import addOperator , divideOperator
print(addOperator(10,10))
print(divideOperator(10,10))

from operators import addOperator as ao , divideOperator as do
print(ao(10,10))
print(do(10,10))