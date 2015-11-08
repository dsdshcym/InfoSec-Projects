def bits_to_int(bits):
    """
    Transform a 0, 1 list to a integer
    """
    return int(bits_to_str(bits), 2)

def int_to_bits(x, n = 0):
    """
    Transform a integer to a n-length 0, 1 list
    Pads 0 if n > len(bin(x))
    Raises ValueError if n < len(bin(x))
    """
    b = map(int, list(bin(x)[2:]))
    if n is 0:
        return b
    if len(b) > n:
        raise ValueError
    return [0 for _ in xrange(n - len(b))] + b

def bits_to_str(bits):
    """
    Transform a 0, 1 list to a string
    """
    return ''.join(map(str, bits))
