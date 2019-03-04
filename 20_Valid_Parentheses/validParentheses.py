# given a string containing just the characters ,determine if the input string is valid.
# an input string is valid if:
# 1. Open brackets must be closed by the same type of brackets
# 2. Open brackets must be closed in the correct order.
def isValid(s):
    stack = []
    dict = {"]": "[", "}": "{", ")": "("}
    for char in s:
        if char in dict.values():
            stack.append(char)
        elif char in dict.keys():
            if stack == [] or dict[char] != stack.pop():
                return False
        else:
            return False
    return stack == []


input = "([)]"
isValid(input)


# about dict
# def aboutDict(s):
#     a = dict(one=1, two=2, three=3)
#     b = {'one': 1, 'two': 2, 'three': 3}
#     c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
#     d = dict([('two', 2), ('one', 1), ('three', 3)])
#     e = dict({'three': 3, 'one': 1, 'two': 2})
#     if a == b == c == d == e:
#         return s
#     else:
#         return False

# another solution,but use more runtime
def isValid(self, s):
    while '[]' in s or '()' in s or '{}' in s:
        s = s.replace('[]', '').replace('()', '').replace('{}', '')
    return not len(s)
