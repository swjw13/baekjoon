# https://www.acmicpc.net/problem/2213
# 트리의 독립집합

import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

conn = defaultdict(set)
for _ in range(N - 1):
    start, end = list(map(int, input().split()))
    conn[start - 1].add(end - 1)
    conn[end - 1].add(start - 1)

queue = deque([(0, 0, 1), (1, lst[0], 1)])
mx = 0
vs = 0
while queue:
    visited, total, cur_point = queue.popleft()
    if cur_point == N:
        if total > mx:
            mx = total
            vs = visited
    else:
        queue.append((visited, total, cur_point + 1))
        tmp = True
        idx = 1
        for i in range(cur_point):
            if idx & visited == idx and cur_point in conn[i]:
                tmp = False
                break
            idx *= 2

        if tmp:
            queue.append((idx ^ visited, total + lst[cur_point], cur_point + 1))

sys.stdout.write("%d\n" % mx)
idx = 1
for i in range(N):
    if idx & vs == idx:
        sys.stdout.write("%d " % (i + 1))
    idx *= 2
