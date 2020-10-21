#!/usr/bin/env python
# coding=utf-8
# @File    : length_of_last_word.py
# @Date    : 2020-10-21
# @Author  : shengjia
def lengthOfLastWord(s):
    if s == "" or s.split() == []:
        return 0
    else:
        print(len(s.split().pop()))


if __name__ == '__main__':
    s = '  '
    lengthOfLastWord(s)
