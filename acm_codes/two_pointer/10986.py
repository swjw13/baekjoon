# https://www.acmicpc.net/problem/10986
# 나머지 합

import sys
from collections import defaultdict
input = sys.stdin.readline

N, M = list(map(int, input().split()))
lst = list(map(int, input().split()))
dic = defaultdict(set)
sub_total = 0
for i in range(N):
    sub_total += lst[i]
    dic[sub_total % M].add(i)

ans = 0
for i in dic.keys():
    n = len(dic[i])
    if n >= 2:
        ans += n * (n - 1) // 2

ans += len(dic[0])
print(ans)