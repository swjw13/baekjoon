import sys
from collections import deque

input = sys.stdin.readline
dydx = [(1, 0), (-1, 0), (0, 1), (0, -1)]

N = int(input())
mp_original = [[] for _ in range(N)]
mp_RGConcat = [[] for _ in range(N)]

for i in range(N):
    line = list(input())[:-1]
    for color in line:
        mp_original[i].append(["R", "G", "B"].index(color) + 1)

        if color in ["R", "G"]:
            mp_RGConcat[i].append(1)
        else:
            mp_RGConcat[i].append(2)


def bfs(lst):
    count = 0

    for i in range(N):
        for j in range(N):
            if lst[i][j] != 0:
                tmp = lst[i][j]
                queue = deque([(i, j)])
                lst[i][j] = 0

                while queue:
                    row, col = queue.popleft()
                    for (dx, dy) in dydx:
                        x = row + dx
                        y = col + dy
                        if 0 <= x < N and 0 <= y < N and lst[x][y] == tmp:
                            queue.append((x, y))
                            lst[x][y] = 0
                count += 1

    return count


original = bfs(mp_original)
concat = bfs(mp_RGConcat)

print(original, concat)
