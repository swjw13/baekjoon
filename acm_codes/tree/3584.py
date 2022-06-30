# https://www.acmicpc.net/problem/3584
# 가장 가까운 공통 조상

import sys
from collections import defaultdict, deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    tree = defaultdict(int)
    height = dict()
    tree_reverse = defaultdict(set)
    for _ in range(N - 1):
        parent, child = list(map(int, input().split()))
        tree[child] = parent
        tree_reverse[parent].add(child)

    root = 1
    while tree[root] != 0:
        root = tree[root]

    queue = deque([(root, 1)])
    height[root] = 1
    while queue:
        cur_point, cur_height = queue.popleft()
        for child in tree_reverse[cur_point]:
            height[child] = cur_height + 1
            queue.append((child, cur_height + 1))

    start1, start2 = list(map(int, input().split()))

    while start1 != start2:
        if height[start1] > height[start2]:
            start1 = tree[start1]
        elif height[start1] < height[start2]:
            start2 = tree[start2]
        else:
            start1 = tree[start1]
            start2 = tree[start2]

    print(start1)