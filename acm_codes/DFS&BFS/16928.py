# 사다리 게임
# https://www.acmicpc.net/problem/16928

import sys
from collections import deque

input = sys.stdin.readline

N, M = list(map(int, input().split()))
ladders = {i: i for i in range(1, 101)}
for _ in range(N):
    start, end = list(map(int, input().split()))
    ladders[start] = end
for _ in range(M):
    start, end = list(map(int, input().split()))
    ladders[start] = end
visited = [False for _ in range(101)]

queue = deque([(1, 0)])
visited[1] = True
while queue:
    current_point, turn = queue.popleft()

    if current_point == 100:
        print(turn)
        break

    for i in range(1, 7):
        if current_point + i < 101:
            if not visited[ladders[current_point + i]]:
                queue.append((ladders[current_point + i], turn + 1))
                visited[ladders[current_point + i]] = True
