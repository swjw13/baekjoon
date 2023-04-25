# https://www.acmicpc.net/problem/4179
# 불!
import sys
from collections import deque

input = sys.stdin.readline
dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

R, C = list(map(int, input().split()))
board = []
jihun_point = None
fire_point = deque()
fire = [[-1 for _ in range(C)] for _ in range(R)]

for row in range(R):
    line = list(input().strip())
    for col in range(C):
        if line[col] == "J":
            jihun_point = (row, col)
        elif line[col] == "F":
            fire[row][col] = 0
            fire_point.append((row, col, 0))
    board.append(line)

while fire_point:
    fire_row, fire_col, cur_turn = fire_point.popleft()
    for dx, dy in dxdy:
        new_row = fire_row + dx
        new_col = fire_col + dy
        if 0 <= new_row < R and 0 <= new_col < C and board[new_row][new_col] != "#":
            if fire[new_row][new_col] == -1:
                fire[new_row][new_col] = cur_turn + 1
                fire_point.append((new_row, new_col, cur_turn + 1))

res = -1
j_queue = deque([(jihun_point[0], jihun_point[1], 0)])
visited = [[False for _ in range(C)] for _ in range(R)]
visited[jihun_point[0]][jihun_point[1]] = True
is_out = False

while j_queue and not is_out:
    cur_row, cur_col, cur_turn = j_queue.popleft()
    for dx, dy in dxdy:
        new_row = cur_row + dx
        new_col = cur_col + dy
        if 0 <= new_row < R and 0 <= new_col < C:
            if board[new_row][new_col] != "#":
                if (fire[new_row][new_col] == -1 or fire[new_row][new_col] > cur_turn + 1) and not visited[new_row][new_col]:
                    visited[new_row][new_col] = True
                    j_queue.append((new_row, new_col, cur_turn + 1))
        else:
            res = cur_turn + 1
            is_out = True
            break
if res == -1:
    print("IMPOSSIBLE")
else:
    print(res)