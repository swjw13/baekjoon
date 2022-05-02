# https://www.acmicpc.net/problem/1764
# 듣보잡 수

import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline

N, M = list(map(int, input().split()))


def create_key(str):
    key = 0
    for i in str:
        key = key * 17 + ord(i)

    return key % 1000

key_table = defaultdict(set)

for _ in range(N):
    a = input().split("\n")[0]
    key = create_key(a)
    key_table[key].add(a)

ans = []
for _ in range(M):
    b = input().split("\n")[0]
    key = create_key(b)
    if b in key_table[key]:
        heapq.heappush(ans, b)
length = len(ans)

print(length)
for i in range(length):
    tmp = heapq.heappop(ans)
    print(tmp)
