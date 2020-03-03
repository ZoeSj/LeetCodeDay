# @File    : merge_sorted_array.py
# @Date    : 2020-03-03
# @Author  : shengjia
class Solution(object):
    def merge(self, A, m, B, n):
        """
        :type A: List[int]
        :type m: int
        :type B: List[int]
        :type n: int
        :rtype: None Do not return anything, modify A in-place instead.
        """
        A[m:] = B
        A.sort()
