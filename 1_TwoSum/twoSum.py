# @File    : twoSum.py
# @Date    : 2019-02-17
# @Author  : shengjia
num = [1, 5, 5, 11]
target = 9


def twoSum(num, target):
    for i in range(len(num)):
        for j in range(1, len(num)):
            while num[i] + num[j] == target and i != j:
                return [i, j]
            else:
                return False


# use the target subtract the value in num
def twoSumFast(num, target):
    if len(num) <= 1:
        return False
    buff_dict = {}
    for i in range(len(num)):
        if num[i] in buff_dict:
            return [buff_dict[num[i]], i]
        else:
            buff_dict[target - num[i]] = i


print(twoSum(num, target))
