# https://www.acmicpc.net/problem/1644
# 소수의 연속 합

import sys


N = int(sys.stdin.readline())
p = [i for i in range(N + 1)]
for i in range(2, int(N ** 0.5) + 1):
    for tmp in range(2 * i, N + 1, i):
        p[tmp] = 0

prime = []
for i in range(2, N + 1):
    if p[i] != 0:
        prime.append(i)

if len(prime) == 0:
    print(0)
else:
    answer = 0
    start = 0
    end = 0
    total_sum = prime[0]

    while end < len(prime):
        if start > end:
            break
        if total_sum == N:
            answer += 1
            total_sum -= prime[start]
            start += 1
            end += 1
            if end < len(prime):
                total_sum += prime[end]
        elif total_sum < N:
            end += 1
            if end < len(prime):
                total_sum += prime[end]
        else:
            total_sum -= prime[start]
            start += 1

    print(answer)
