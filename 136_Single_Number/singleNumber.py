# @File    : singleNumber.py
# @Date    : 2019-04-01
# @Author  : shengjia

list = [2, 2, 3, 4, 1, 1, 7, -1, 7, 6, 6, 4, 3]


def singleNumber(list):
    list = sorted(list)
    result = com(list)
    while result[0] == 0:
        result = com(list)
        if result[0] == 1:
            return result[1]

    print(result[1])


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
