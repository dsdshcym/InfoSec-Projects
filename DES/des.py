# -*- coding: utf-8 -*-
from random import randint
import argparse
import sys
import getpass

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

def len_to_8bits(x):
    b = map(int, list(bin(x)[2:]))
    return [0 for _ in xrange(8 - len(b))] + b

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

def Feistel(bits, key):
    # 扩展置换表，将 32位 扩展至 48位
    E = [31, 0,  1,  2,  3,  4,
         3,  4,  5,  6,  7,  8,
         7,  8,  9,  10, 11, 12,
         11, 12, 13, 14, 15, 16,
         15, 16, 17, 18, 19, 20,
         19, 20, 21, 22, 23, 24,
         23, 24, 25, 26, 27, 28,
         27, 28, 29, 30, 31, 0]

    # S盒，每个S盒是4x16的置换表，6位 -> 4位
    S_BOX = [
        [
            [14, 4,  13, 1,  2,  15, 11, 8,  3,  10, 6,  12, 5,  9,  0,  7],
            [0,  15, 7,  4,  14, 2,  13, 1,  10, 6,  12, 11, 9,  5,  3,  8],
            [4,  1,  14, 8,  13, 6,  2,  11, 15, 12, 9,  7,  3,  10, 5,  0],
            [15, 12, 8,  2,  4,  9,  1,  7,  5,  11, 3,  14, 10, 0,  6,  13]
        ],
        [
            [15, 1,  8,  14, 6,  11, 3,  4,  9,  7,  2,  13, 12, 0,  5,  10],
            [3,  13, 4,  7,  15, 2,  8,  14, 12, 0,  1,  10, 6,  9,  11, 5],
            [0,  14, 7,  11, 10, 4,  13, 1,  5,  8,  12, 6,  9,  3,  2,  15],
            [13, 8,  10, 1,  3,  15, 4,  2,  11, 6,  7,  12, 0,  5,  14, 9]
        ],
        [
            [10, 0,  9,  14, 6,  3,  15, 5,  1,  13, 12, 7,  11, 4,  2,  8],
            [13, 7,  0,  9,  3,  4,  6,  10, 2,  8,  5,  14, 12, 11, 15, 1],
            [13, 6,  4,  9,  8,  15, 3,  0,  11, 1,  2,  12, 5,  10, 14, 7],
            [1,  10, 13, 0,  6,  9,  8,  7,  4,  15, 14, 3,  11, 5,  2,  12]
        ],
        [
            [7,  13, 14, 3,  0,  6,  9,  10, 1,  2,  8,  5,  11, 12, 4,  15],
            [13, 8,  11, 5,  6,  15, 0,  3,  4,  7,  2,  12, 1,  10, 14, 9],
            [10, 6,  9,  0,  12, 11, 7,  13, 15, 1,  3,  14, 5,  2,  8,  4],
            [3,  15, 0,  6,  10, 1,  13, 8,  9,  4,  5,  11, 12, 7,  2,  14]
        ],
        [
            [2,  12, 4,  1,  7,  10, 11, 6,  8,  5,  3,  15, 13, 0,  14, 9],
            [14, 11, 2,  12, 4,  7,  13, 1,  5,  0,  15, 10, 3,  9,  8,  6],
            [4,  2,  1,  11, 10, 13, 7,  8,  15, 9,  12, 5,  6,  3,  0,  14],
            [11, 8,  12, 7,  1,  14, 2,  13, 6,  15, 0,  9,  10, 4,  5,  3]
        ],
        [
            [12, 1,  10, 15, 9,  2,  6,  8,  0,  13, 3,  4,  14, 7,  5,  11],
            [10, 15, 4,  2,  7,  12, 9,  5,  6,  1,  13, 14, 0,  11, 3,  8],
            [9,  14, 15, 5,  2,  8,  12, 3,  7,  0,  4,  10, 1,  13, 11, 6],
            [4,  3,  2,  12, 9,  5,  15, 10, 11, 14, 1,  7,  6,  0,  8,  13]
        ],
        [
            [4,  11, 2,  14, 15, 0,  8,  13, 3,  12, 9,  7,  5,  10, 6,  1],
            [13, 0,  11, 7,  4,  9,  1,  10, 14, 3,  5,  12, 2,  15, 8,  6],
            [1,  4,  11, 13, 12, 3,  7,  14, 10, 15, 6,  8,  0,  5,  9,  2],
            [6,  11, 13, 8,  1,  4,  10, 7,  9,  5,  0,  15, 14, 2,  3,  12]
        ],
        [
            [13, 2,  8,  4,  6,  15, 11, 1,  10, 9,  3,  14, 5,  0,  12, 7],
            [1,  15, 13, 8,  10, 3,  7,  4,  12, 5,  6,  11, 0,  14, 9,  2],
            [7,  11, 4,  1,  9,  12, 14, 2,  0,  6,  10, 13, 15, 3,  5,  8],
            [2,  1,  14, 7,  4,  10, 8,  13, 15, 12, 9,  0,  3,  5,  6,  11]
        ]
    ]

    # P置换，32位 -> 32位
    P = [15, 6,  19, 20,
         28, 11, 27, 16,
         0,  14, 22, 25,
         4,  17, 30, 9,
         1,  7,  23, 13,
         31, 26, 2,  8,
         18, 12, 29, 5,
         21, 10, 3,  24]

    bits = selfReplacement(bits, E)
    bits = xor(bits, key)
    result = []
    for i in xrange(8):
        bits_i = bits[6 * i : 6 * (i + 1)]
        x = bits_to_int([bits_i[0], bits_i[5]])
        y = bits_to_int(bits_i[1:5])
        result += int_to_4bits(S_BOX[i][x][y])
    return selfReplacement(result, P)

def des(bits, keys):
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

    bits = selfReplacement(bits, IP)
    left = bits[:32]
    right = bits[32:]
    for i in xrange(encrypt_times):
        temp = right
        right = xor(left, Feistel(right, keys[i]))
        left = temp
    return selfReplacement(right + left, IP_1)

def encrypt(bits):
    pre_bits = IV
    cipher = []
    final = False
    while bits:
        now = bits[:64]
        bits = bits[64:]
        N = len(now)
        if N <= 56:
            padding_len = 56 - N
            padding_len_bits = len_to_8bits(padding_len)
            now += [randint(0, 1) for _ in xrange(padding_len)] + padding_len_bits
        if 56 < N <= 64 and bits == []:
            padding_len = 56 + 64 - N
            padding_len_bits = len_to_8bits(padding_len)
            now += [randint(0, 1) for _ in xrange(64 - N)]
            bits = [randint(0, 1) for _ in xrange(56)] + padding_len_bits
            final = True
        pre_bits = des(xor(pre_bits, now), keys)
        cipher += pre_bits
        if final:
            pre_bits = des(xor(pre_bits, bits), keys)
            cipher += pre_bits
            break

    return cipher

def decrypt(bits, key):
    return xor(des(bits[:64], keys[:encrypt_times][::-1]), IV)

def perror(error):
    print >> sys.stderr, error
    exit()

def main():
    parser = argparse.ArgumentParser(
        description = 'DES Encrypt or Decrypt at the command line')
    parser.add_argument(
        '-d', '--decrypt', action = 'store_true', default = False)
    parser.add_argument(
        'file', type = argparse.FileType('r'),
        help = 'The file that needed encrypt or decrypt')
    parser.add_argument(
        '-i', '--IV',
        default =
        '0111010001001111000001100100010010100011000001001010011001010100',
        help = 'Change the default Init Vector')
    parser.add_argument(
        '-r', '--encrypt_round', type = int, default = 6)
    parser.add_argument(
        '-o', '--output', type = argparse.FileType('w'),
        default = sys.stdout,
        help = 'The file where the encrypt/decrypt results should be written')
    args = parser.parse_args()
    is_decrypt = args.decrypt

    global encrypt_times
    encrypt_times = args.encrypt_round
    if encrypt_times < 0 or encrypt_times > 16:
        perror("Encrypt Times must be in range 0 to 16 (included)")

    global IV
    IV = args.IV
    if set(IV) != set(['0', '1']):
        perror("IV must be a binary")
    if len(IV) != 64:
        perror("IV must be a 64 bits binary")

    bits = str.strip(args.file.readline())
    if set(bits) != set(['0', '1']):
        perror("The input must be a binary")

    key = getpass.getpass('Please Enter the Key: ')
    if set(key) != set(['0', '1']):
        perror("The key must be a binary")
    if len(key) != 64:
        perror("The key must be a 64 bits binary")

    bits = map(int, list(bits))
    key = map(int, list(key))
    IV = map(int, list(IV))

    global keys
    keys = generateKeys(key)

    if is_decrypt:
        args.output.write(''.join(str(x) for x in decrypt(bits, key)) + '\n')
    else:
        args.output.write(''.join(str(x) for x in encrypt(bits)) + '\n')

if __name__ == '__main__':
    main()
