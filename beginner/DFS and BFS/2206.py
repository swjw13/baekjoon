# bfs -> 맵은 최대한 건드리지 않는 걸로

from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = list(map(int, input().split()))
mp = []
visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(2)]

for _ in range(N):
    line = list(input())
    mp.append(list(map(int, line[:-1])))

queue = deque([(0, 0, 1, 1)])
visited[1][0][0] = True
dydx = [(1, 0), (-1, 0), (0, 1), (0, -1)]

count = -1
answers = []
while queue:
    row, col, turn, ability = queue.popleft()

    if row == N - 1 and col == M - 1:
        answers.append(turn)

    for dx, dy in dydx:
        x = row + dx
        y = col + dy

        if 0 <= x < N and 0 <= y < M:
            if mp[x][y] == 0 and not visited[ability][x][y]:
                queue.append((x, y, turn + 1, ability))
                visited[ability][x][y] = True
            elif mp[x][y] == 1 and ability == 1 and not visited[ability][x][y]:
                queue.append((x, y, turn + 1, 0))
                visited[0][x][y] = True

if len(answers) == 0:
    print(-1)
else:
    print(min(answers))
