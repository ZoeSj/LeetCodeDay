# @File    : singleNumber.py
# @Date    : 2019-04-01
# @Author  : shengjia
import operator

list = [2, 2, 3, 4, 1, 1, 7, 5, 7, 6, 6, 4, 3]


def singleNumber(list):
    list = sorted(list)
    result = com(list)
    while result[0] == 0:
        result = com(list)
    if result[0] == 1:
        return result[1]


def com(list):
    if len(list) == 1:
        return [1, list[0]]
    elif list[0] - list[1] == 0:
        list.remove(list[0])
        list.remove(list[0])
        return [0]
    elif list[0] - list[1] < 0:
        return [1, list[0]]


print(singleNumber(list))


def singleNumber1(nums):
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0) + 1
    for key, val in dic.items():
        if val == 1:
            return key


def singleNumber2(nums):
    res = 0
    for num in nums:
        res ^= num
    return res


def singleNumber3(nums):
    return 2 * sum(set(nums)) - sum(nums)


def singleNumber4(nums):
    return reduce(lambda x, y: x ^ y, nums)


def singleNumber(nums):
    return reduce(operator.xor, nums)

