# @File    : reverseInteger.py
# @Date    : 2019-02-17
# @Author  : shengjia

num = 1234
output = 54321


def reverseInteger(num):
    if num < -2147483648 or num > 2147483648 or num == 0:
        return 0
    b = list(str(num))

    def popZone(list):
        for key in range(len(list)):
            while list[key] == '0':
                list.pop(0)
            return list

    if len(b) % 2 != 0:
        b.append('0')
    if b[0] == '-':
        title = b[0]
        b.pop(0)
    else:
        title = ''
    j = len(b) - 1

    for i in range(0, len(b) / 2):
        b[i], b[j] = b[j], b[i]
        i = i + 1
        j = j - 1

    popZone(b)
    result = int(title + "".join(b))
    print(int(result))
    while result < -2147483648 or result > 2147483648:
        return 0
    else:
        return result


print(reverseInteger(num))

# ls = ['0', '5', '4', '3', '2', '1']
#
# str4 = "".join(ls)
# print map(int, ls)
# print(str4)
