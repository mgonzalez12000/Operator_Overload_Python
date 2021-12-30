# Marco Gonzalez
# CS 3035-01
# Module includes data fields and a constructor. This module emphasizes to handle "magic" methods to allow
# operation overload to take place

import math
import doctest


class Vector:
    __a = 1
    __b = 1
    __c = 1

    def __init__(self, __a, __b, __c):
        self.__a = __a
        self.__b = __b
        self.__c = __c

    def __str__(self):
        """
        Returns a string represenation of your vector

        Args:
            self (Vector): object

        Returns:
            str: '<a, b, c>'

        Examples:
            >>> vector = Vector(2, 4, 3)
            >>> vector.__str__()
            '<2, 4, 3>'

            >>> vector_2 = Vector(1, 2, 3)
            >>> vector_2.__str__()
            '<1, 2, 3>'

            >>> vector_3 = Vector(2, 5, 7)
            >>> vector_3.__str__()
            '<2, 5, 7>'
        """
        return '<' + str(self.__a) + ', ' + str(self.__b) + ", " + str(self.__c) + '>'

    def __repr__(self):
        """
        Returns a string representation of the Vector class

        Args:
            self (Vector): object

        Returns:
            str: 'Vector(2, 4, 3)'

        Examples:
            >>> vector = Vector(2, 4, 3)
            >>> vector.__repr__()
            'Vector(2, 4, 3)'

            >>> vector_2 = Vector(1, 2, 3)
            >>> vector_2.__repr__()
            'Vector(1, 2, 3)'

            >>> vector_3 = Vector(2, 5, 7)
            >>> vector_3.__repr__()
            'Vector(2, 5, 7)'
        """
        return 'Vector(' + str(self.__a) + ', ' + str(self.__b) + ', ' + str(self.__c) + ')'

    def magnitude(self):
        """
        Returns the magnitude of the given Vector object

        Args:
            self (Vector): object

        Returns:
            int: sqrt(a^2 + b^2 + c^2)

        Examples:
            >>> vector = Vector(2, 4, 3)
            >>> vector.magnitude()
            5.385164807134504

            >>> vector_2 = Vector(1, 2, 3)
            >>> vector_2.magnitude()
            3.7416573867739413

            >>> vector_3 = Vector (2, 5, 7)
            >>> vector_3.magnitude()
            8.831760866327848
        """
        magnitude = math.sqrt(math.pow(self.__a, 2) + math.pow(self.__b, 2) + math.pow(self.__c, 2))
        return magnitude

    def __eq__(self, vector_2):
        """
        Returns True if both vectors are equivalent, returns False if both vectors are not equivalent

        Args:
            self (Vector): object
            vector_2 (Vector): object

        Returns:
            Bool: True
            Bool: False

        Examples:
            >>> vector = Vector(2, 4, 3)
            >>> vector_two = Vector(1, 3, 1)
            >>> vector == vector_two
            False
            >>> vector_3 = Vector (2, 4, 3)
            >>> vector == vector_3
            True
        """
        vector_1 = self.__a, self.__b, self.__c
        if vector_1 == vector_2:
            return True
        else:
            return False

    # + overloading
    def __add__(self, vector_2):
        """
        Returns a new object of Vector after addition

        Args:
            self (Vector): object
            vector_2 (Vector): object

        Returns:
            Vector: <(self.a + vector_2.a), (self.b + vector_2.b), (self.c -+ vector_2.v)>

        Examples:
            >>> vector = Vector(2, 4, 3)
            >>> vector_two = Vector(1, 3, 1)
            >>> vector + vector_two
            Vector(3, 7, 4)

            >>> vector_3 = Vector(1 , 4, 2)
            >>> vector + vector_3
            Vector(3, 8, 5)

            >>> vector_4 = Vector(1, 1, 1)
            >>> vector_3 + vector_4
            Vector(2, 5, 3)
        """
        return Vector((self.__a + vector_2.__a), (self.__b + vector_2.__b), (self.__c + vector_2.__c))

    # += overloading
    def __iadd__(self, vector_2):
        """
        Returns a string of a vector after addition

        Args:
            self (Vector): object
            vector_2 (Vector): object

        Returns:
            str: <(self.a - vector_2.a), (self.b - vector_2.b), (self.c - vector_2.v)>

        Examples:
            >>> vector = Vector(2, 4, 3)
            >>> vector_two = Vector(1, 3, 1)
            >>> vector += vector_two
            >>> print(vector)
            <3, 7, 4>

            >>> vector_3 = Vector (1, 1, 1)
            >>> vector_3 += vector
            >>> print(vector_3)
            <4, 8, 5>

            >>> vector_4 = Vector(2, 2, 2)
            >>> vector_5 = Vector(3, 1, 3)
            >>> vector_5 += vector_4
            >>> print (vector_5)
            <5, 3, 5>
        """
        self.__a += vector_2.__a
        self.__b += vector_2.__b
        self.__c += vector_2.__c
        return self

    # - overloading
    def __sub__(self, vector_2):
        """
        Returns a new object of Vector after subtraction

        Args:
            self (Vector): object
            vector_2 (Vector): object

        Returns:
            Vector: <(self.a - vector_2.a), (self.b - vector_2.b), (self.c - vector_2.v)>

        Examples:
            >>> vector = Vector(2, 4, 3)
            >>> vector_two = Vector(1, 3, 1)
            >>> vector - vector_two
            Vector(1, 1, 2)

            >>> vector_3 = Vector(1 , 4, 2)
            >>> vector - vector_3
            Vector(1, 0, 1)

            >>> vector_4 = Vector(1 , 1, 1)
            >>> vector_3 - vector_4
            Vector(0, 3, 1)
        """
        return Vector((self.__a - vector_2.__a), (self.__b - vector_2.__b), (self.__c - vector_2.__c))

    # -= overloading
    def __isub__(self, vector_2):
        """
        Returns a string of a vector

        Args:
            self (Vector): object
            vector_2 (Vector): object

        Returns:
            str: <(self.a - vector_2.a), (self.b - vector_2.b), (self.c - vector_2.v)>

        Examples:
            >>> vector = Vector(2, 4, 3)
            >>> vector_two = Vector(1, 3, 1)
            >>> vector -= vector_two
            >>> print(vector)
            <1, 1, 2>

            >>> vector_3 = Vector (1, 1, 1)
            >>> vector_two -= vector_3
            >>> print(vector_3)
            <1, 1, 1>

            >>> vector_4 = Vector (5, 6, 3)
            >>> vector_5 = Vector (2, 1, 3)
            >>> vector_4 -= vector_5
            >>> print(vector_4)
            <3, 5, 0>
        """
        self.__a -= vector_2.__a
        self.__b -= vector_2.__b
        self.__c -= vector_2.__c
        return self

    # * overloading
    def __mul__(self, vector_2):
        """
        If both opearnds are Vector objects:
            returns an int after multplication
        If one operand is a Vector and the other operand is an interger:
            returns a new Vector result

        Args:
            self (Vector): object
            vector_2 (Vector): object
            vector_2: int

        Returns:
            int: <(self.a * vector_2.a), (self.b * vector_2.b), (self.c * vector_2.v)>
            Vector: (self.a * vector_2.a), (self.b * vector_2.b), (self.c * vector_2.v)
        Examples:
            >>> vector = Vector(2, 4, 3)
            >>> vector_two = Vector(1, 3, 1)
            >>> vector * vector_two
            17

            >>> vector_3 = 2
            >>> vector * vector_3
            Vector(4, 8, 6)
        """
        if type(self) == type(vector_2):
            return (self.__a * vector_2.__a) + (self.__b * vector_2.__b) + (self.__c * vector_2.__c)
        else:
            return Vector((self.__a * vector_2), (self.__b * vector_2), (self.__c * vector_2))

    # Checks if the instance of vector_2 is an int
    def __rmul__(self, vector_2):
        """
        Check if the first operand is an integer
            returns a new Vector result

        Args:
            self (Vector): object
            vector_2: int

        Returns:
            Vector: (self.a * vector_2.a), (self.b * vector_2.b), (self.c * vector_2.v)
        Examples:
            >>> vector = Vector(2, 4, 3)
            >>> vector_3 = 2
            >>> vector_3 * vector
            Vector(4, 8, 6)
        """
        if isinstance(vector_2, int):
            return Vector((self.__a * vector_2), (self.__b * vector_2), (self.__c * vector_2))

    # *= overloading
    def __imul__(self, vector_2):
        """
        Returns the scalar multplication of a vector

        Args:
            self (Vector): object
            vector_2 (int): value

        Returns:
            str: <(self.a * vector_2.a), (self.b * vector_2.b), (self.c * vector_2.v)>

        Examples:
            >>> vector = Vector(2, 4, 3)
            >>> print(vector * 2)
            <4, 8, 6>

            >>> vector_two = Vector(1, 1, 1)
            >>> print(vector_two * 5)
            <5, 5, 5>

            >>> vector_3 = Vector(10, 5, 14)
            >>> print(vector_3 * 2)
            <20, 10, 28>
        """
        self.__a *= vector_2
        self.__b *= vector_2
        self.__c *= vector_2
        return self

    # % overloading
    def __mod__(self, vector_2):
        """
        Returns a new Vector object of the cross porduct of two vectors

        Args:
            self (Vector): object
            vector_2 (Vector): object

        Returns:
            Vector: ((self.__b * vector_2.__c) - (self.__c * vector_2.__b)),
                    ((self.__c * vector_2.__a) - (self.__a * vector_2.__c)),
                    ((self.__a * vector_2.__b) - (self.__b * vector_2.__a)))
        Examples:
            >>> vector = Vector(2, 4, 3)
            >>> vector_two = Vector(1, 3, 1)
            >>> print(vector % vector_two)
            <-5, 1, 2>

            >>> vector_3 = Vector(1, 1, 1)
            >>> print(vector % vector_3)
            <1, 1, -2>

            >>> vector_4 = Vector(2, 7, 1)
            >>> print(vector_3 % vector_4)
            <-6, 1, 5>
        """
        return Vector(((self.__b * vector_2.__c) - (self.__c * vector_2.__b)),
                      ((self.__c * vector_2.__a) - (self.__a * vector_2.__c)),
                      ((self.__a * vector_2.__b) - (self.__b * vector_2.__a)))

    # [] overloading
    def __getitem__(self, vector_2):
        """
        Returns a, b, c of the vector

        Args:
            self (Vector): object
            vector_2 (Vector): object

        Returns int: position

        Examples:
            >>> vector = Vector(1, 3, 1)
            >>> print(vector[1])
            3

            >>> vector_two = Vector(2, 5, 1)
            >>> print(vector_two[2])
            1

            >>> vector_3 = Vector(3, 5, 5)
            >>> print(vector_3[0])
            3
        """
        if vector_2 == 0:
            return self.__a
        elif vector_2 == 1:
            return self.__b
        elif vector_2 == 2:
            return self.__c

    # [] overloading
    def __setitem__(self, vector_2, value):
        """
        Returns a change made to a, b, c of the vector

        Args:
            self (Vector): object
            vector_2 (Vector): object

        Returns vector represenation with value at index changed

        Examples:
            >>> vector = Vector(2, 4, 3)
            >>> vector[1] = 100
            >>> print(vector[1])
            100
            >>> print(vector)
            <2, 100, 3>

            >>> vector_two = Vector(1, 3, 5)
            >>> vector_two[0] = 2
            >>> print(vector_two[0])
            2
            >>> print(vector_two)
            <2, 3, 5>

            >>> vector_3 = Vector(10, 15, 7)
            >>> vector_3[2] = 0
            >>> print(vector_3[2])
            0
            >>> print(vector_3)
            <10, 15, 0>
        """
        if vector_2 == 0:
            self.__a = value
        elif vector_2 == 1:
            self.__b = value
        elif vector_2 == 2:
            self.__c = value


doctest.testmod()
