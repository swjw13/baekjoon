from collections import deque
import sys

input = sys.stdin.readline
dydx = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dfs(board, n):
    count = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                queue = deque([(i, j)])
                while queue:
                    row, col = queue.popleft()
                    for dx, dy in dydx:
                        x = row + dx
                        y = col + dy
                        if 0 <= x < n and 0 <= y < n and board[x][y]:
                            queue.append((x, y))
                            board[x][y] = False
                count += 1
    return count


N = int(input())
mp = []
max_height = 0
for _ in range(N):
    line = list(map(int, input().split()))
    tmp = max(line)
    if tmp > max_height:
        max_height = tmp
    mp.append(line)

max_ground = 1

for i in range(max_height):
    tmp = [[False for _ in range(N)] for _ in range(N)]

    for row in range(N):
        for col in range(N):
            if mp[row][col] >= 2:
                mp[row][col] -= 1
                tmp[row][col] = True
            elif mp[row][col] == 1:
                mp[row][col] -= 1

    c = dfs(tmp, N)
    if max_ground < c:
        max_ground = c

print(max_ground)