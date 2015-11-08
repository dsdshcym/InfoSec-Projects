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
