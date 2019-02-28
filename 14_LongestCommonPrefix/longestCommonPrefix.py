# @File    : longestCommonPrefix.py
# @Date    : 2019-02-19
# @Author  : shengjia

list1 = ["flower", "flow", "flight"]
out = "fl"

list2 = ["dog", "racecar", "car"]
out1 = ""


def longestCommonPrefix(strs):
    if not strs:
        return ""

    for i, letter_group in enumerate(zip(*strs)):
        if len(set(letter_group)) > 1:
            return strs[0][:i]
    else:
        return min(strs)


print(longestCommonPrefix(list2))
