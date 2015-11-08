def euclid(x, y):
    while x != 0:
        x, y = y % x, x
    return y

def extended_euclid(x, y):
    pass
