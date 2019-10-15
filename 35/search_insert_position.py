# @File    : search_insert_position.py
# @Date    : 2019-10-15
# @Author  : shengjia
# describe : Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.You may assume no duplicates in the array.
# Example 1:
#
# Input: [1,3,5,6], 5
# Output: 2
# Example 2:
#
# Input: [1,3,5,6], 2
# Output: 1

def searchInsertPosition(nums, target):
    for i in range(0, len(nums)):
        if nums[i] == target:
            print(i, 1)
            return i
    nums.append(target)
    nums.sort()
    for i in range(0, len(nums)):
        if target == nums[i]:
            print(i, 2)
            return i


lists = [1, 3, 5, 6]
target = 0
searchInsertPosition(lists, target)
