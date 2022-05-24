# 빠른 곱셈
import sys

A, B, C = list(map(int, sys.stdin.readline().split()))


def fast(p, q, r):
    if q == 1:
        return p % r
    elif q == 0:
        return 1
    else:
        return ((fast(p, q // 2, r) ** 2) * fast(p, q % 2, r)) % r


a = fast(A, B, C)
print(a)
