# https://www.acmicpc.net/problem/1926
# 그림

import sys
from collections import deque

input = sys.stdin.readline
dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

n, m = list(map(int, input().split()))
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

total = 0
mx = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            queue = deque([(i, j)])
            board[i][j] = 0
            count = 1
            while queue:
                cur_row, cur_col = queue.popleft()
                for dx, dy in dxdy:
                    new_row = cur_row + dx
                    new_col = cur_col + dy
                    if 0 <= new_row < n and 0 <= new_col < m and board[new_row][new_col] == 1:
                        count += 1
                        board[new_row][new_col] = 0
                        queue.append((new_row, new_col))
            total += 1
            mx = max(mx, count)

print(total)
print(mx)
