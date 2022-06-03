# https://www.acmicpc.net/problem/11509
# 풍선 맞추기

import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

memory = defaultdict(int)

for i in lst:
    if memory[i] == 0:
        memory[i - 1] += 1
    else:
        memory[i] -= 1
        memory[i - 1] += 1

count = 0
for key, value in memory.items():
    if value != 0:
        count += value
print(count)