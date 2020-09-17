import os
from itertools import *
import operator

# Enter your code here.

# product
def func1(w, x, y, z):
    a = [w,x]
    b = [y,z]
    prod = product(a,b, repeat=2)
    return list(prod)


# permutation
def func2(*a):
    perm = permutations(a)
    return list(perm)


# combination
def func3(*a):
    comb =combinations(a,2)
    return list(comb)

# combination with replacement
def func4(*a):
    comb_wr = combinations_with_replacement(a,2)
    return list(comb_wr)


# accumulate
def func5(*a):
    accum = accumulate(a, min)
    return list(accum)

    '''For testing the code, no input is to be provided'''


if __name__ == "__main__":
    a, b, c, d = list(map(int, input().split()))
    x = func1(a, b, c, d)
    print(x)

    a, b, c = list(map(int, input().split()))
    x = func2(a, b, c)
    print(x)

    a, b, c = list(map(int, input().split()))
    x = func3(a, b, c)
    print(x)


    a, b, c = list(map(int, input().split()))
    x = func4(a, b, c)
    print(x)

    a, b, c, d, e = list(map(int, input().split()))
    x = func5(a, b, c, d, e)
    print(x)