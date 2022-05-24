# 숨바꼭질
# https://www.acmicpc.net/problem/13913

import sys
from collections import deque

input = sys.stdin.readline

N, K = list(map(int, input().split()))
visited = [-1 for _ in range(100001)]
visited[N] = N
queue = deque([N])

while queue:
    current_point = queue.popleft()

    if current_point == K:
        prev_point = deque()
        check_point = current_point
        while check_point != N:
            prev_point.appendleft(check_point)
            check_point = visited[check_point]

        print(len(prev_point))
        prev_point.appendleft(N)

        for i in prev_point:
            print(i, end=' ')
        break

    if current_point - 1 >= 0 and visited[current_point - 1] == -1:
        queue.append(current_point - 1)
        visited[current_point - 1] = current_point

    if current_point + 1 < 100001 and visited[current_point + 1] == -1:
        queue.append(current_point + 1)
        visited[current_point + 1] = current_point

    if 2 * current_point < 100001 and visited[current_point * 2] == -1:
        queue.append(2 * current_point)
        visited[2 * current_point] = current_point
