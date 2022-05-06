# https://www.acmicpc.net/problem/1976
# 여행 가자

import sys

input = sys.stdin.readline


N = int(input())
M = int(input())

parent = {i: i for i in range(N + 1)}


def find_parent(point):
    if parent[point] != point:
        parent[point] = find_parent(parent[point])
    return parent[point]


for i in range(N):
    line = list(map(int, input().split()))
    for j in range(i, N):
        if line[j] == 1:
            a = find_parent(i + 1)
            b = find_parent(j + 1)

            parent[a] = min(a, b)
            parent[b] = min(a, b)

travel = list(map(int, input().split()))
ans = "YES"
for i in range(M - 1):
    a = find_parent(travel[i])
    b = find_parent(travel[i + 1])
    if a != b:
        ans = "NO"
        break
print(ans)
