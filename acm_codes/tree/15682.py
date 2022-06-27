# https://www.acmicpc.net/problem/15681
# 트리와 쿼리

import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

N, R, Q = list(map(int, input().split()))
tree = defaultdict(set)
visited = [False for _ in range(N + 1)]
count = defaultdict(int)

for _ in range(N - 1):
    start, end = list(map(int, input().split()))
    tree[start].add(end)
    tree[end].add(start)


def tree_travel(cur_point):
    visited[cur_point] = True

    if len(tree[cur_point]) == 1:
        if cur_point == R:
            tmp = 0
            for i in tree[cur_point]:
                tmp += tree_travel(i)
            count[cur_point] = tmp + 1
            return tmp + 1

        else:
            count[cur_point] = 1
            return 1

    else:
        tmp = 0
        for i in tree[cur_point]:
            if not visited[i]:
                tmp += tree_travel(i)
        count[cur_point] = tmp + 1
        return tmp + 1


tree_travel(R)

for _ in range(Q):
    tmp = int(input())
    print(count[tmp])