# 이모티콘 이어 붙이기
# https://www.acmicpc.net/problem/14226

import sys
from collections import deque

input = sys.stdin.readline
MAX_SIZE = 1500


S = int(input())
heap = deque([(0, 1, 0)])
visited = [sys.maxsize for _ in range(MAX_SIZE + 1)]
visited[1] = 0
count = 1

while True:
    if count == MAX_SIZE + 1:
        break

    time, point, clipboard = heap.popleft()

    if point - 1 >= 0:
        if visited[point - 1] == sys.maxsize:
            count += 1
        heap.append((time + 1, point - 1, clipboard))
        visited[point - 1] = min(visited[point - 1], time + 1)

    if point + clipboard <= MAX_SIZE:
        if visited[point + clipboard] == sys.maxsize:
            count += 1
        heap.append((time + 1, point + clipboard, clipboard))
        visited[point + clipboard] = min(visited[point + clipboard], time + 1)
    if 2 * point <= MAX_SIZE and time + 2 < visited[2 * point]:
        if visited[2 * point] == sys.maxsize:
            count += 1
        heap.append((time + 2, 2 * point, point))
        visited[2 * point] = min(visited[2 * point], time + 2)

print(visited[S])
