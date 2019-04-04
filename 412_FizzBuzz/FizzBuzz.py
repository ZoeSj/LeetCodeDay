# @File    : FizzBuzz.py
# @Date    : 2019-04-04
# @Author  : shengjia

def fizzBuzz(n):
    list = []
    for i in range(1, n + 1):
        if i % 3 == 0:
            list.append('Fizz')
        elif i % 5 == 0:
            list.append('Buzz')
        elif i % 15 == 0:
            list.append('FizzBuzz')
        else:
            list.append(str(i))
    return list


print(fizzBuzz(17))
