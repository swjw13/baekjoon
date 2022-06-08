# https://www.acmicpc.net/problem/20040
# 사이클 게임

import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10 ** 6)

N, M = list(map(int, input().split()))
parent = [i for i in range(N)]


def find_parent(p1):
    if parent[p1] != p1:
        parent[p1] = find_parent(parent[p1])
    return parent[p1]


def union(p1, p2):
    p1 = find_parent(p1)
    p2 = find_parent(p2)

    final_parent = min(p1, p2)
    parent[p1] = final_parent
    parent[p2] = final_parent

ans = 0
for i in range(M):
    a, b = list(map(int, input().split()))
    parent1 = find_parent(a)
    parent2 = find_parent(b)
    if parent1 == parent2:
        ans = i + 1
        break
    else:
        union(parent1, parent2)

print(ans)