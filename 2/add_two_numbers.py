# @File    : add_two_numbers.py
# @Date    : 2019-09-03
# @Author  : shengjia
l1 = [2, 4, 3]
l2 = [5, 6, 4]


def addTwoNumbers(l1, l2):
    s1 = map(str, reverse(l1))
    num1 = int("".join(s1))
    s2 = map(str, reverse(l2))
    num2 = int("".join(s2))

    sum = map(int, reverse(str(num1 + num2)))

    return sum


def reverse(l):
    j = len(l) - 1
    ls = []
    for i in range(0, len(l)):
        ls.append(l[j])
        j = j - 1
    return ls


print(addTwoNumbers(l1, l2))
