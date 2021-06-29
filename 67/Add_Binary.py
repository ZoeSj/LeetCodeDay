"""
Given two binary strings a and b, return their sum as a binary string.
"""


def addBinary_1(a, b):
    a = int(a, 2)
    b = int(b, 2)
    ab = bin(a + b)

    print(ab[2:])


def addBinary_2(a, b):
    result = ''
    if len(a) > len(b):
        length = len(a)
    elif len(b) > len(a):
        length = len(b)
    else:
        length = len(a)
    a = a.zfill(length + 1)
    b = b.zfill(length + 1)
    bit = 0

    for i in range(length + 1):
        j = length - i
        sum_num = int(a[j]) + int(b[j])
        if bit != 0 and j < length:
            sum_num += bit
            bit = 0

        if sum_num == 0:
            result += '0'
        elif sum_num == 1:
            result += '1'
        elif sum_num == 2:
            result += '0'
            bit = 1
        elif sum_num == 3:
            result += '1'
            bit = 1
    return str(int(result[::-1]))


addBinary_2('1111', '1111')
