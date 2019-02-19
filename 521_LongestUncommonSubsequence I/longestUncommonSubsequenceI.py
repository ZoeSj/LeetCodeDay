# @File    : longestUncommonSubsequenceI.py
# @Date    : 2019-02-19
# @Author  : shengjia

str1 = "ccc"
str2 = "ngkbgbdqgfvasrwqlmibkuzvavnsoircrboiqipdpbqwssmoiflmsyvzxdcfuduaunmifrstgnkcsrfclkumkngmykhzceoeqcpm"


def longestUncommonSubsquence(a, b):
    if a == b:
        return -1
    elif len(b) < len(a):
        return len(a)
    else:
        return len(b)


def longestUncommonSubsquenceOther(a, b):
    if a == b:
        return -1
    return max(len(a), len(b))


print(longestUncommonSubsquenceOther(str1, str2))
