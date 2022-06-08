# https://www.acmicpc.net/problem/1774
# 우주신과의 교감

import sys
import heapq

input = sys.stdin.readline

N, M = list(map(int, input().split()))
parent = [i for i in range(N + 1)]

def find_parent(p):
    if parent[p] != p:
        parent[p] = find_parent(parent[p])
    return parent[p]


def union(p1, p2):
    p1 = find_parent(p1)
    p2 = find_parent(p2)

    p = min(p1, p2)
    parent[p1] = p
    parent[p2] = p


def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


gods = []
for _ in range(N):
    gods.append(list(map(int, input().split())))

for _ in range(M):
    a, b = list(map(int, input().split()))
    union(a - 1, b - 1)

lines = []
for i in range(N):
    for j in range(i, N):
        lines.append([distance(gods[i][0], gods[i][1], gods[j][0], gods[j][1]), i, j])

heapq.heapify(lines)
length = len(lines)
ans = 0

for _ in range(length):
    tmp = heapq.heappop(lines)
    a = find_parent(tmp[1])
    b = find_parent(tmp[2])
    if a != b:
        ans += tmp[0]
        union(a, b)

print("%.2f" % ans)
