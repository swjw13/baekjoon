# https://www.acmicpc.net/problem/1806
# 부분합

import sys
input = sys.stdin.readline

N, S = list(map(int, input().split()))
lst = list(map(int, input().split()))

start = 0
end = 0
count = lst[0]
mn = sys.maxsize

while end < N:
    if start > end:
        break

    if count == S:
        mn = min(mn, end - start + 1)
        count -= lst[start]
        start += 1
        end += 1
        if end < N:
            count += lst[end]
    elif count < S:
        end += 1
        if end < N:
            count += lst[end]
    else:
        mn = min(mn, end - start + 1)
        count -= lst[start]
        start += 1

if mn == sys.maxsize:
    print(0)
else:
    print(mn)