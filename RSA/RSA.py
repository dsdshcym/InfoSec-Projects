from math import log

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
    pass
