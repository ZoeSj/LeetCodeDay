# @File    : count_and_say.py
# @Date    : 2019-10-22
# @Author  : shengjia
# the count and say sequence is the sequence of integers with the first five terms as following:
# 1.    1
# 2.    11
# 3.    21
# 4.    1211
# 5.    111221
# given an integer n where 1=<n<=30,generate n(th) term of the count and say sequence.

def count_and_say(num):
    s = '1'
    for _ in range(num - 1):
        let, temp, count = s[0], '', 0
        for l in s:
            if let == l:
                count += 1
            else:
                temp += str(count) + let
                let = l
                count = 1
        temp += str(count) + let
        s = temp
    print(s)
    return s


count_and_say(6)
