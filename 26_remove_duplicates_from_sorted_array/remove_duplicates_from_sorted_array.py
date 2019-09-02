# @File    : remove_duplicates_from_sorted_array.py
# @Date    : 2019-09-02
# @Author  : shengjia

nums = [1, 1, 2]


def removeDuplicates(num):
    j = 0
    for i in range(1, len(num)):
        if num[i] != num[j]:
            j += 1
            num[j] = num[i]
    return j + 1


print(removeDuplicates(nums))
