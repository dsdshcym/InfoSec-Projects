# -*- coding: utf-8 -*-

def leftShift(bits, step):
    return bits[step:] + bits[:step]

def selfReplacement(bits, replace_table):
    new_bits = list(bits)
    for i, pos in enumerate(replace_table):
        new_bits[i] = bits[pos]
    return new_bits

def xor(list_A, list_B):
    if len(list_A) != len(list_B):
        raise BaseException
    ans = []
    for i in range(len(list_A)):
        ans.append(list_A[i] ^ list_B[i])
    return ans

def generateKeys(key):
    # 密钥置换表，将64位密钥变成56位
    IPC = [56, 48, 40, 32, 24, 16, 8,
           0,  57, 49, 41, 33, 25, 17,
           9,  1,  58, 50, 42, 34, 26,
           18, 10, 2,  59, 51, 43, 35,
           62, 54, 46, 38, 30, 22, 14,
           6,  61, 53, 45, 37, 29, 21,
           13, 5,  60, 52, 44, 36, 28,
           20, 12, 4,  27, 19, 11, 3]

    # 压缩置换，将56位密钥压缩成48位子密钥
    PC = [13, 16, 10, 23, 0,  4,
          2,  27, 14, 5,  20, 9,
          22, 18, 11, 3,  25, 7,
          15, 6,  26, 19, 12, 1,
          40, 51, 30, 36, 46, 54,
          29, 39, 50, 44, 32, 47,
          43, 48, 38, 55, 33, 52,
          45, 41, 49, 35, 28, 31]

    SHIFT_STEPS = [1, 1, 2, 2, 2, 2, 2, 2,
                   1, 2, 2, 2, 2, 2, 2, 1]

    short_key = selfReplacement(key, IPC)
    C = short_key[:28]
    D = short_key[28:]
    keys = []
    for i in xrange(encrypt_times):
        C = leftShift(C, SHIFT_STEPS[i])
        D = leftShift(D, SHIFT_STEPS[i])
        keys.append(selfReplacement(C + D, PC))
    return keys
