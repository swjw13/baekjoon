# https://www.acmicpc.net/problem/2470
# 알칼리 용액

import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

lst.sort()

start = 0
end = N - 1
mx = sys.maxsize
mx_tmp = [0,0]
while start < end:
    value = lst[start] + lst[end]

    if value < 0:
        if mx > abs(value):
            mx = abs(value)
            mx_tmp = [lst[start], lst[end]]
        start += 1
    else:
        if mx > value:
            mx = value
            mx_tmp = [lst[start], lst[end]]
        end -= 1

print("{} {}".format(mx_tmp[0], mx_tmp[1]))