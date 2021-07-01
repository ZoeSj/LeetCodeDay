def climb(n):
    temp1 = 1
    temp2 = 2
    if n == 1:
        return temp1
    elif n == 2:
        return temp2
    for i in range(n - 3, -1, -1):
        temp = temp2 + temp1
        temp1 = temp2
        temp2 = temp
    print(temp)
    return temp


climb(7)
