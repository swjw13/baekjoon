# https://www.acmicpc.net/problem/1922
# 네트워크 연결

import sys
import heapq

# sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

N = int(input())
M = int(input())

parent = [i for i in range(N + 1)]
heap = []


def find_parent(a):
    if parent[a] != a:
        parent[a] = find_parent(parent[a])
    return parent[a]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    fin = min(a, b)
    parent[a] = fin
    parent[b] = fin


for _ in range(M):
    p1, p2, dist = list(map(int, input().split()))
    heapq.heappush(heap, (dist, p1, p2))

cnt = 0
while heap:
    d, p1, p2 = heapq.heappop(heap)

    a = find_parent(p1)
    b = find_parent(p2)

    if a != b:
        union(a, b)
        cnt += d

print(cnt)
