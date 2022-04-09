#https://www.acmicpc.net/problem/3273
# 두 수의 합
# 투 포인터

import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
k = int(input())

lst.sort()

start = 0
end = N - 1
ans = 0
while True:
    if start >= end:
        break
    value = lst[start] + lst[end]
    if value == k:
        ans += 1
        start += 1
        end -= 1
    elif value < k:
        start += 1
    else:
        end -= 1

print(ans)