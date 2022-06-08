# https://www.acmicpc.net/problem/2887
# 행성 터널

import sys
import heapq

input = sys.stdin.readline

N = int(input())
points = []
points_dict = dict()
for i in range(N):
    tmp = tuple(map(int, input().split()))
    points.append(tmp)
    points_dict[tmp] = i

parent = [i for i in range(N)]


def find_parent(p):
    if parent[p] != p:
        parent[p] = find_parent(parent[p])
    return parent[p]


def union(p1, p2):
    p1 = find_parent(p1)
    p2 = find_parent(p2)

    tmp = min(p1, p2)
    parent[p1] = tmp
    parent[p2] = tmp


lst1 = sorted(points, key=lambda x: x[0])
lst2 = sorted(points, key=lambda x: x[1])
lst3 = sorted(points, key=lambda x: x[2])

lines = []

for i in range(N - 1):
    lines.append([abs(lst1[i][0] - lst1[i + 1][0]), points_dict[lst1[i]], points_dict[lst1[i + 1]]])
    lines.append([abs(lst2[i][1] - lst2[i + 1][1]), points_dict[lst2[i]], points_dict[lst2[i + 1]]])
    lines.append([abs(lst3[i][2] - lst3[i + 1][2]), points_dict[lst3[i]], points_dict[lst3[i + 1]]])

ans = 0
heapq.heapify(lines)
for _ in range(len(lines)):
    tmp = heapq.heappop(lines)
    a = find_parent(tmp[1])
    b = find_parent(tmp[2])
    if a != b:
        ans += tmp[0]
        union(a, b)

print(ans)
