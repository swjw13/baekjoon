# https://www.acmicpc.net/problem/1946
# 신입 사원

import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    numbers = []
    seconds = [i for i in range(1, N + 1)]
    for _ in range(N):
        numbers.append(list(map(int, input().split())))

    numbers.sort(key=lambda x: x[0])
    threshold = 100001
    cnt = 0
    for i in numbers:
        if i[1] < threshold:
            threshold = i[1]
            cnt += 1
    print(cnt)