# https://www.acmicpc.net/problem/4386
# 별자리 만들기

import sys
import heapq

input = sys.stdin.readline

N = int(input())
stars = []
for i in range(N):
    stars.append(list(map(float, input().split())))

parent = [i for i in range(N)]


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


lines = []
for i in range(N):
    for j in range(i + 1, N):
        lines.append([distance(stars[i][0], stars[i][1], stars[j][0], stars[j][1]), i, j])
heapq.heapify(lines)

ans = 0
length = len(lines)
for _ in range(length):
    tmp = heapq.heappop(lines)
    a = find_parent(tmp[1])
    b = find_parent(tmp[2])

    if a != b:
        ans += tmp[0]
        union(a, b)

print("%.2f" % ans)
