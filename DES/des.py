# -*- coding: utf-8 -*-

def leftShift(bits, step):
    return bits[step:] + bits[:step]

def selfReplacement(bits, replace_table):
    new_bits = []
    for pos in replace_table:
        new_bits.append(bits[pos])
    return new_bits

def xor(list_A, list_B):
    if len(list_A) != len(list_B):
        raise BaseException
    ans = []
    for i in range(len(list_A)):
        ans.append(list_A[i] ^ list_B[i])
    return ans

def bits_to_int(bits):
    result = 0
    for bit in bits:
        result = (result << 1) | bit
    return result

def int_to_4bits(x):
    result = []
    while x != 0:
        result.append(x & 1)
        x >>= 1
    result += [0 for i in xrange(4 - len(result))]
    return result[::-1]

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

def encrypt(bits, key):
    IP = [57, 49, 41, 33, 25, 17, 9,  1,
          59, 51, 43, 35, 27, 19, 11, 3,
          61, 53, 45, 37, 29, 21, 13, 5,
          63, 55, 47, 39, 31, 23, 15, 7,
          56, 48, 40, 32, 24, 16, 8,  0,
          58, 50, 42, 34, 26, 18, 10, 2,
          60, 52, 44, 36, 28, 20, 12, 4,
          62, 54, 46, 38, 30, 22, 14, 6]

    IP_1 = [39, 7, 47, 15, 55, 23, 63, 31,
            38, 6, 46, 14, 54, 22, 62, 30,
            37, 5, 45, 13, 53, 21, 61, 29,
            36, 4, 44, 12, 52, 20, 60, 28,
            35, 3, 43, 11, 51, 19, 59, 27,
            34, 2, 42, 10, 50, 18, 58, 26,
            33, 1, 41, 9,  49, 17, 57, 25,
            32, 0, 40, 8,  48, 16, 56, 24]

    keys = generateKeys(key)

    bits = selfReplacement(bits, IP)
    left = bits[:32]
    right = bits[32:]
    for i in xrange(encrypt_times):
        temp = right
        right = xor(left, Feistel(right, keys[i]))
        left = temp
    return selfReplacement(right + left, IP_1)
