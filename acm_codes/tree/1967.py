# https://www.acmicpc.net/problem/1967
# 트리의 지름

import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

tree = defaultdict(dict)
connection = defaultdict(list)

N = int(input())
for _ in range(N - 1):
    parent, child, weight = list(map(int, input().split()))
    tree[parent][child] = weight
    connection[parent].append(child)

mx = -sys.maxsize


def dfs(cur_point):
    global mx
    if len(tree[cur_point]) >= 2:
        childs = connection[cur_point]
        lst = []
        for i in childs:
            p = tree[cur_point][i] + dfs(i)
            lst.append(p)
        lst.sort()
        mx = max(mx, lst[-1] + lst[-2])

        return lst[-1]

    elif len(tree[cur_point]) == 1:
        child = connection[cur_point][0]
        p = tree[cur_point][child] + dfs(child)
        mx = max(mx, p)
        return p
    else:
        return 0


if N == 1:
    print(0)
else:
    dfs(1)
    print(mx)
