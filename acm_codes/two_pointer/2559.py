# https://www.acmicpc.net/problem/2559
# 수열

import sys

N, K = list(map(int, input().split()))
lst = list(map(int, input().split()))

start = 0
end = K - 1
part_sum = sum(lst[start:end + 1])
max_sum = -sys.maxsize

while end < len(lst):
    print(part_sum)
    max_sum = max(max_sum, part_sum)

    part_sum -= lst[start]
    start += 1

    end += 1
    if end < len(lst):
        part_sum += lst[end]


print(max_sum)