#!/usr/bin/env python
# coding=utf-8
# @File    : is_str_resort.py
# @Date    : 2021-01-13
# @Author  : shengjia

def is_str_resort(s1, s2):
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False


string_one = 'abc'
string_two = 'bca'

is_str_resort(string_one, string_two)
