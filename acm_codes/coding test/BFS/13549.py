# 숨바꼭질 3
# https://www.acmicpc.net/problem/13549

import sys
from collections import deque

input = sys.stdin.readline
N, K = list(map(int, input().split()))

queue = deque([(N, 0)])
dist = [sys.maxsize for _ in range(100001)]
dist[N] = 0

while queue:
    current_point, curret_dist = queue.popleft()

    if current_point == K:
        print(curret_dist)
        break

    if current_point - 1 >= 0 and dist[current_point - 1] > curret_dist + 1:
        dist[current_point - 1] = curret_dist + 1
        queue.append((current_point - 1, curret_dist + 1))
    if current_point + 1 <= 100000 and dist[current_point + 1] > curret_dist + 1:
        dist[current_point + 1] = curret_dist + 1
        queue.append((current_point + 1, curret_dist + 1))
    if 2 * current_point <= 100000 and dist[2 * current_point] > curret_dist:
        dist[current_point * 2] = curret_dist
        queue.appendleft((current_point * 2, curret_dist))
