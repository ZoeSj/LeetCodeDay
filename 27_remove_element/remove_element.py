# @File    : remove_element.py
# @Date    : 2019-09-03
# @Author  : shengjia
nums = [0, 1, 2, 2, 3, 0, 4, 2]
nu = 2


def removeElement(num, n):
    while n in num:
        num.remove(n)
    return num


print(removeElement(nums, nu))
