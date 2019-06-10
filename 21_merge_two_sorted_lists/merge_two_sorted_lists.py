# @File    : merge_two_sorted_lists.py
# @Date    : 2019-04-28
# @Author  : shengjia

list_one = [1, 2, 4]
list_two = [1, 3, 4]


def mergeTwoLists(list1, list2):
    list = list1 + list2
    list.sort()
    return list


mergeTwoLists(list_one, list_two)



# Time:  O(n)
# Space: O(1)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution(object):
#     # iteratively
#     def mergeTwoLists(self, l1, l2):
#         dummy = cur = ListNode(0)
#         while l1 and l2:
#             if l1.val < l2.val:
#                 cur.next = l1
#                 l1 = l1.next
#             else:
#                 cur.next = l2
#                 l2 = l2.next
#             cur = cur.next
#         cur.next = l1 or l2
#         return dummy.next
