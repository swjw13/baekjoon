from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
dydx = [(2, -1), (2, 1), (-2, -1), (-2, 1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

T = int(input())
for _ in range(T):
    I = int(input())
    board = [[0 for _ in range(I)] for _ in range(I)]
    start_r, start_c = list(map(int, input().split()))
    end_r, end_c = list(map(int, input().split()))
    queue = deque([(start_r, start_c, 0)])
    board[start_r][start_c] = 1
    while queue:
        (row, col, turn) = queue.popleft()
        if row == end_r and col == end_c:
            print(turn)
            break
        for (dy, dx) in dydx:
            x = row + dy
            y = col + dx
            if 0 <= x < I and 0 <= y < I and board[x][y] == 0:
                queue.append((x, y, turn + 1))
                board[x][y] = 1
