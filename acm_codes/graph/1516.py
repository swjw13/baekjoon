# https://www.acmicpc.net/problem/1516
# 게임 개발

import sys
from collections import defaultdict, deque
import heapq
input = sys.stdin.readline

connected = defaultdict(list)
in_point = defaultdict(int)
time = defaultdict(int)

start_point = []

N = int(input())

for i in range(N):
    lst = list(map(int, input().split()))
    cur_time = lst[0]
    cur_point = i + 1

    time[cur_point] = cur_time
    in_point[cur_point] = len(lst) - 2

    if in_point[cur_point] == 0:
        start_point.append((cur_time, cur_point))
    else:
        for i in lst[1:-1]:
            connected[i].append(cur_point)

final_dist = defaultdict(int)

while start_point:
    t, p = heapq.heappop(start_point)
    final_dist[p] = max(final_dist[p], t)
    for con in connected[p]:
        in_point[con] -= 1
        if in_point[con] == 0:
            heapq.heappush(start_point, (t + time[con], con))

for i in range(1, N + 1):
    print(final_dist[i])