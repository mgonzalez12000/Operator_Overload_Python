# Marco Gonzalez
# CS 3035-01
# The driver or 'main' module that creates instances of an object Vector and handles operation overload
# Module also handles memory allocation for operation overloads such as += -= *= by using deepcopy()
# Video explanation: https://calstatela.instructuremedia.com/embed/66e6f73f-4d71-4496-907f-5f73db2aebaa

# Upon your request to explain changes made on resubmission, they are as follows:
# In the vector.py module, class Vector, the dunder method __rmul__ was integrated to check if the instance of the
# first operand was an integer. This allows for commutative scalar multiplication to work (Eg: V * S and S * V).
# Docstrings and Doctests were also added in the dunder method __rmul__

# On line 37 of this current module, vector_tester.py, * operator overload was called when the first operand
# is an integer and the second operand is a Vector object to check if the correct output was yielded.

from vector import Vector
from copy import deepcopy


def main():
    vector = Vector(2, 4, 3)
    print('Printing vector:', vector.__str__())
    print('Overloading the debugging string method:', vector.__repr__())
    print("The vector's magnitude is:", vector.magnitude())
    vector_2 = Vector(1, 3, 1)
    print('== operator overload:', vector == vector_2)
    print('+ operator overload:', vector + vector_2)
    vector_plus_eq = deepcopy(vector)
    vector_plus_eq += vector_2
    print('+= operator overload:', vector_plus_eq)
    print('- operator overload:', vector - vector_2)
    vector_minus_eq = deepcopy(vector)
    vector_minus_eq -= vector_2
    print('-= operator overload:', vector_minus_eq)
    print('* operator overload for dot product (two vector operands):', vector * vector_2)
    print('* overload for scalar multiplication (one vector operand and one integer operand):', vector * 2)
    print('* overload for COMMUTATIVE scalar multiplication (one integer operand and one vector operand):', 2 * vector)
    vector_mul_eq = deepcopy(vector)
    vector_mul_eq *= 2
    print('*= operator overload:', vector_mul_eq)
    print('% operator overload:', vector % vector_2)
    print('get item using [] overload:', vector_2[1])
    print('original vector:', vector_2)
    vector_2[1] = 100
    print('set item using [] overload:', vector_2[1])
    print('new set vector is', vector_2)


if __name__ == "__main__":
    main()
