# @File    : twoSum.py
# @Date    : 2019-02-17
# @Author  : shengjia
num = [3, 2, 4]
target = 6

def twoSum(num, target):
    for i in range(len(num)):
        for j in range(1, len(num)):
            while num[i] + num[j] == target and i != j:
                return [i, j]


# use the target subtract the value in num
# def twoSumFast(num, target):
#     if len(num) <= 1:
#         return False
#     buff_dict = {}
#     for i in range(len(num)):
#         if num[i] in buff_dict:
#             return [buff_dict[num[i]], i]
#         else:
#             buff_dict[target - num[i]] = i

def twoSums(num, target):
    j = -1
    for i in range(len(num)):
        k = target - num[i]
        nums = num[:i]
        if k in nums:
            j = nums.index(k)
            break
    if j>=0:
        return[j,i]


print(twoSums(num, target))
