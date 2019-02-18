# @File    : romanToInteger.py
# @Date    : 2019-02-18
# @Author  : shengjia

num = "MCMXCIV"


def romanToInteger(num):
    sumN = []
    sumNum = 0
    l = ['I', 'V', 'X', 'L', 'C', 'D', 'M', 1000, 500, 100, 50, 10, 5, 1]
    for value in num:
        for i in range(len(l)):
            if value == l[i]:
                sumN.append(l[len(l) - i - 1])

    for m in range(len(sumN)):
        sumN.append(0)
        if sumN[m] < sumN[m + 1] and sumN[m] != 0:
            number = sumN[m + 1] - sumN[m]
            sumNum = sumNum + number
            sumN.pop(m)
            sumN.insert(m, 0)
            sumN.pop(m + 1)
            sumN.insert(m + 1, 0)

        elif sumN[m] > sumN[m + 1] and sumN[m] != 0:
            sumNum = sumNum + sumN[m]
            sumN.pop(m)
            sumN.insert(m, 0)

        elif sumN[m] == sumN[m + 1] and sumN[m] != 0:
            sumNum = sumNum + sumN[m + 1] + sumN[m]
            sumN.pop(m)
            sumN.insert(m, 0)
            sumN.pop(m + 1)
            sumN.insert(m + 1, 0)
    return sumNum


class Solution(object):
    def romanToInt(self, s):
        sumN = []
        sumNum = []
        l = ['I', 'V', 'X', 'L', 'C', 'D', 'M', 1000, 500, 100, 50, 10, 5, 1]
        for value in s:
            for i in range(len(l)):
                if value == l[i]:
                    sumN.append(l[len(l) - i - 1])

        for m in range(len(sumN)):
            sumN.append(0)
            if sumN[m] < sumN[m + 1] and sumN[m] != 0:
                number = sumN[m + 1] - sumN[m]
                sumNum.append(number)
                sumN.pop(m)
                sumN.insert(m, 0)
                sumN.pop(m + 1)
                sumN.insert(m + 1, 0)

            elif sumN[m] >= sumN[m + 1] and sumN[m] != 0:
                sumNum.append(sumN[m])
                sumN.pop(m)
                sumN.insert(m, 0)

        return sum(sumNum)


def romanToIntWay(num):
    roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    z = 0
    for i in range(len(num) - 1):
        if roman[num[i]] < roman[num[i + 1]]:
            z -= roman[num[i]]
        else:
            z += roman[num[i]]
    return z + roman[num[-1]]


print(romanToIntWay(num))
