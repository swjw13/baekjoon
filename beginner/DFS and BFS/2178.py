from collections import deque
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N, M = list(map(int, input().split()))
mp = []

for _ in range(N):
    mp.append(list(map(int, input()[:-1])))

dydx = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(row, col):
    queue = deque([(row, col, 0)])
    mp[row][col] = 0
    while queue:
        row, col, depth = queue.popleft()
        if row == N - 1 and col == M - 1:
            return depth
        for (dx, dy) in dydx:
            x = row + dy
            y = col + dx
            if 0 <= x < N and 0 <= y < M and mp[x][y] == 1:
                queue.append((x, y, depth + 1))
                mp[x][y] = 0


d = bfs(0, 0)
print(d + 1)
