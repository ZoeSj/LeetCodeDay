# @File    : palindromeNumber.py
# @Date    : 2019-02-18
# @Author  : shengjia

number = -121
output = True


def palindromeNumber(num):
    x = cmp(num, 0)
    r = int(`x * num`[::-1])
    if num < 0:
        return False
    else:
        if num == r:
            return True
        else:
            return False


def palindromeNum(num):
    b = list(str(num))

    print(b[0])


print(palindromeNum(number))
