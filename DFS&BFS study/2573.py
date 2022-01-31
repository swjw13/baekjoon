from collections import deque
import sys

input = sys.stdin.readline
dydx = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(board, n, m):
    count = 0
    for i in range(n):
        for j in range(m):
            if board[i][j]:
                queue = deque([(i, j)])
                board[i][j] = False
                while queue:
                    row, col = queue.popleft()
                    for dx, dy in dydx:
                        x = row + dx
                        y = col + dy
                        if 0 <= x < n and 0 <= y < m and board[x][y]:
                            queue.append((x, y))
                            board[x][y] = False
                count += 1
            if count > 1:
                return count
    return count


n, m = list(map(int, input().split()))
mp = []
for _ in range(n):
    mp.append(list(map(int, input().split())))

turn = 0
while True:
    turn += 1
    tmp = [[False for _ in range(m)] for _ in range(n)]
    tmp2 = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if mp[i][j] > 0:
                for (dy, dx) in dydx:
                    if 0 <= i + dy < n and 0 <= j + dx < m and mp[i + dy][j + dx] <= 0:
                        tmp2[i][j] += 1

    for i in range(n):
        for j in range(m):
            mp[i][j] -= tmp2[i][j]
            if mp[i][j] > 0:
                tmp[i][j] = True
    count = bfs(tmp, n, m)

    if count == 0:
        print(0)
        break
    elif count > 1:
        print(turn)
        break
