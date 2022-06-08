# https://www.acmicpc.net/problem/9372
# 상근이의 여행

import sys

input = sys.stdin.readline

T = int(input())


def find_parent(lst, p1):
    if lst[p1] != p1:
        lst[p1] = find_parent(lst, lst[p1])
    return lst[p1]


def union(lst, p1, p2):
    p1 = find_parent(lst, p1)
    p2 = find_parent(lst, p2)

    tmp = min(p1, p2)
    lst[p1] = tmp
    lst[p2] = tmp


for _ in range(T):
    N, M = list(map(int, input().split()))
    parent = [i for i in range(N + 1)]
    ans = 0
    for _ in range(M):
        p1, p2 = list(map(int, input().split()))
        a = find_parent(parent, p1)
        b = find_parent(parent, p2)

        if a != b:
            ans += 1
        union(parent, p1, p2)

    print(ans)