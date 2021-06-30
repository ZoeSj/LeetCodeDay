def mySqrtBuiltPow(x):
    result = pow(x, 0.5)
    print(result)


def mySqrtBuiltInt(x):
    result = int(x ** 0.5)
    print(result)


def mySqrt(x):
    n = 0
    left = 0
    right = 0
    if x == 0:
        print(0)
        return 0
    while n <= 2147483648:
        left = n * n
        right = left + 2 * n
        n += 1
        if left < x < right:
            print(n - 1)
        elif x == left or x == right:
            print(n - 1)
            return n - 1


def mySqrt_second(x):
    if x < 2:
        return x
    left = 0
    right = x
    n = 0
    while left <= right:
        n += 1
        if n * n <= x < n * (2 + n):
            print(n)
            return n


# print(left)

# mySqrtBuilt(2147483642)
mySqrtBuiltInt(3000000)
mySqrt_second(3000000)
# mySqrt(88)
