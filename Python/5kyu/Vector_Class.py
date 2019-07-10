"""
Instructions:

Create a Vector object that supports addition, subtraction, dot products, and norms. So, for example:

a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
c = Vector([5, 6, 7, 8])

a.add(b)      # should return a new Vector([4, 6, 8])
a.subtract(b) # should return a new Vector([-2, -2, -2])
a.dot(b)      # should return 1*3 + 2*4 + 3*5 = 26
a.norm()      # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
a.add(c)      # raises an exception
If you try to add, subtract, or dot two vectors with different lengths, you must throw an error!

Also provide:

a toString method, so that using the vectors from above, a.toString() === '(1,2,3)'
(in Python, this is a __str__ method, so that str(a) == '(1,2,3)')
an equals method, to check that two vectors that have the same components are equal
Note: the test cases will utilize the user-provided equals method.
"""

from functools import reduce
from math import sqrt


class Vector:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def add(self, vector):
        if len(self.coordinates) != len(vector.coordinates):
            raise IndexError
        return Vector(list(map(lambda x, y: x + y, self.coordinates, vector.coordinates)))

    def subtract(self, vector):
        if len(self.coordinates) != len(vector.coordinates):
            raise IndexError
        return Vector(list(map(lambda x, y: x - y, self.coordinates, vector.coordinates)))

    def dot(self, vector):
        if len(self.coordinates) != len(vector.coordinates):
            raise IndexError
        return reduce(lambda x, y: x + y, list(map(lambda x, y: x*y, self.coordinates, vector.coordinates)))

    def norm(self):
        return sqrt(reduce(lambda x, y: x + y, list(map(lambda x: x ** 2, self.coordinates))))

    def __str__(self):
        return "(" + ','.join([str(i) for i in self.coordinates]) + ")"

    def equals(self, vector):
        return self.coordinates == vector.coordinates


if __name__ == '__main__':
    a = Vector([1, 2, 3])
    b = Vector([3, 4, 5])
    c = Vector([5, 6, 7, 8])

    print(a.add(b))  # should return a new Vector([4, 6, 8])
    print(a.subtract(b))  # should return a new Vector([-2, -2, -2])
    print(a.dot(b))  # should return 1*3 + 2*4 + 3*5 = 26
    print(a.norm())  # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
    print(a.add(c))  # raises an exception
