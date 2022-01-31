from collections import deque

dydx = [(1, 0), (-1, 0), (0, 1), (0, -1)]

R, C = list(map(int, input().split()))
board = []
for _ in range(R):
    board.append(list(input()))

queue = deque([((0, 0), board[0][0])])
mx = 0


def dfs(row, col, prev):
    global mx
    if len(prev) > mx:
        mx = len(prev)
    for (dx, dy) in dydx:
        x = row + dx
        y = col + dy
        if 0 <= x < R and 0 <= y < C and board[x][y] not in prev:
            dfs(x, y, prev + board[x][y])


dfs(0, 0, board[0][0])
print(mx)
