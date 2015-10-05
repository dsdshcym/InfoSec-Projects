# -*- coding: utf-8 -*-

def leftShift(bits, step):
    return bits[step:] + bits[:step]
