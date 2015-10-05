# -*- coding: utf-8 -*-

def leftShift(bits, step):
    return bits[step:] + bits[:step]

def selfReplacement(bits, replace_table):
    new_bits = list(bits)
    for i, pos in enumerate(replace_table):
        new_bits[i] = bits[pos]
    return new_bits
