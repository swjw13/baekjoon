# https://www.acmicpc.net/problem/1766
# 문제집

import sys
import heapq

input = sys.stdin.readline
ans = []

N, M = map(int, input().split())
graph = [set() for _ in range(N + 1)]
count = [0 for _ in range(N + 1)]
heap = []

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].add(end)
    count[end] += 1

for i in range(1, N + 1):
    if count[i] == 0:
        heapq.heappush(heap, i)

while heap:
    tmp = heapq.heappop(heap)
    ans.append(tmp)
    for i in graph[tmp]:
        count[i] -= 1
        if count[i] == 0:
            heapq.heappush(heap, i)

print(" ".join(map(str, ans)))