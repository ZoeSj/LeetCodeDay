# @File    : maximum_subarray.py
# @Date    : 2019-11-08
# @Author  : shengjia

def maxSubArray(nums):
    for i in range(1, len(nums)):
        print(nums[i-1])
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1]
            print(nums[i])
    # print(max(nums))


inputs = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
maxSubArray(inputs)
