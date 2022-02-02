# 이항계수 빠르게

import sys

N, K = list(map(int, sys.stdin.readline().split()))


def find_fact(num):
    total = 1
    for i in range(2, num + 1):
        total = (total * i) % 1000000007
    return total


a = find_fact(N)
b = find_fact(K)
c = find_fact(N - K)

print((a // (b * c)) % 1000000007)
