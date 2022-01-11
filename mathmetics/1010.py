# 다리 놓기
from math import factorial

def comb(num1, num2):
    return factorial(num1) // (factorial(num2) * factorial(num1-num2))

T = int(input())
for _ in range(T):
    N, M = list(map(int, input().split()))
    print(comb(M, N))