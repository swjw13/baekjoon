from math import factorial

N, K = list(map(int, input().split()))
n = N + K - 1
print(factorial(n) // (factorial(N) * factorial(K - 1)) % 1000000000)