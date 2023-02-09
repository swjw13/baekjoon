# https://www.acmicpc.net/problem/2665
# 미로만들기
import heapq
from collections import deque

dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
board = []
INF = 100000

n = int(input())
for _ in range(n):
    line = list(map(int, list(input())))
    board.append(line)

dist = [[INF for _ in range(n)] for _ in range(n)]

queue = deque([(0, 0)])
dist[0][0] = 0
while queue:
    cur_row, cur_col = queue.popleft()

    for movement in dxdy:
        new_row = cur_row + movement[0]
        new_col = cur_col + movement[1]
        if 0 <= new_row < n and 0 <= new_col < n:
            new_dist = dist[cur_row][cur_col] + 1 if board[new_row][new_col] == 0 else dist[cur_row][cur_col]
            if dist[new_row][new_col] > new_dist:
                dist[new_row][new_col] = new_dist
                queue.append((new_row, new_col))

print(dist[n - 1][n - 1])