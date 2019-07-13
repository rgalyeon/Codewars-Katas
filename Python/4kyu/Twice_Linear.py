"""
Instructions:

Consider a sequence u where u is defined as follows:

    1) The number u(0) = 1 is the first one in u.
    2) For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
    3) There are no other numbers in u.

Ex: u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]

1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13, then 7 gives 15 and 22 and so on...
Task:

Given parameter n the function dbl_linear (or dblLinear...) returns the element u(n) of the ordered (with <) sequence u (so, there are no duplicates).
Example:

dbl_linear(10) should return 22
"""


def dbl_linear(n):
    x1, x2 = 0, 0
    u = [1]
    for i in range(n):
        y1 = u[x1] * 2 + 1
        y2 = u[x2] * 3 + 1
        if y1 <= y2:
            u.append(y1)
            x1 += 1
            if y1 == y2:
              x2 += 1
        else:
            u.append(y2)
            x2 += 1
    return u[n]


if __name__ == '__main__':
    print(dbl_linear(10))
    print(dbl_linear(20))
    print(dbl_linear(30))
    print(dbl_linear(50))
