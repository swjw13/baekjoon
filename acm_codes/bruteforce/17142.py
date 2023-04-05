import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline
dxdy = [(-1, 0), (1, 0), (0, 1), (0, -1)]

n, m = list(map(int, input().split()))
lab = []
viruses = []
ans = sys.maxsize
for row in range(n):
    lst = list(map(int, input().split()))

    for col in range(n):
        if lst[col] == 2:
            viruses.append((row, col))

    lab.append(lst)

for i in combinations(viruses, m):
    res = 0
    cur_lab = [[0 for _ in range(n)] for _ in range(n)]
    for row in range(n):
        for col in range(n):
            cur_lab[row][col] = lab[row][col]

    queue = deque()
    for (row, col) in i:
        queue.append((row, col, 0))

    while queue:
        r, c, t = queue.popleft()
        if lab[r][c] != 2:
            res = max(res, t)
        for dx, dy in dxdy:
            new_row = r + dx
            new_col = c + dy
            if 0 <= new_row < n and 0 <= new_col < n:
                if cur_lab[new_row][new_col] == 0:
                    queue.append((new_row, new_col, t + 1))
                    cur_lab[new_row][new_col] = 1
                elif cur_lab[new_row][new_col] == 2:
                    queue.append((new_row, new_col, t + 1))
                    cur_lab[new_row][new_col] = 1

    all_visited = True
    for row in range(n):
        for col in range(n):
            if cur_lab[row][col] == 0:
                all_visited = False
                break
        if not all_visited:
            break
    if all_visited:
        ans = min(ans, res)

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)