from math import log
from random import randint

import sys
sys.path.append('..')

from public import *

def euclid(x, y):
    while x != 0:
        x, y = y % x, x
    return y

def extended_euclid(x, y):
    if (x == 0):
        return y, 0, 1
    else:
        g, b, a = extended_euclid(y % x, x)
        return g, a - (y // x) * b, b

def coPrime(x, y):
    return euclid(x, y) == 1

def extract_two_power(x):
    if x == 0:
        return 0, 0
    two_power = x & (-x)
    return int(log(two_power, 2)), x / two_power

def mod_exp(x, p, m):
    bits = int_to_bits(p)
    max_power = len(bits)
    powers = [x % m]
    for i in xrange(2, max_power + 1):
        powers.append((powers[i - 2] ** 2) % m)
    result = 1
    for i, bit in enumerate(bits[::-1]):
        if bit == 1:
            result = (result * powers[i]) % m
    return result

def Miller_Robin(n, k):
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    s, d = extract_two_power(n - 1)

    def test(a):
        x = mod_exp(a, d, n)
        if x == 1 or x == n - 1:
            return None
        for i in range(1, s):
            x = mod_exp(x, 2, n)
            if x == n - 1:
                return None
        return False

    for i in range(k):
        a = randint(2, n - 1)
        if test(a) == False:
            return False
    return True

def mul_inverse(d, m):
    if coPrime(d, m):
        return extended_euclid(d, m)[1] % m
    else:
        raise ValueError

