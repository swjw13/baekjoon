# 분할정복을 이용한 피보나치

import sys
DIV = 1000000007
prev = dict()

def fibo(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    elif num == 2:
        return 1
    elif num in prev.keys():
        return prev[num]
    else:
        if num % 2 == 0:
            tmp = num // 2
            a = fibo(tmp) % DIV
            c = fibo(tmp - 1) % DIV
            b = (a + c) % DIV
            prev[num] = (a * b + a * c) % DIV
            return prev[num]
        else:
            tmp = num // 2
            a = fibo(tmp - 1) % DIV
            b = fibo(tmp) % DIV
            c = (a + b) % DIV
            d = (b + c) % DIV
            prev[num] = (b * d + a * c) % DIV
            return prev[num]


n = int(sys.stdin.readline())
print(fibo(n))
