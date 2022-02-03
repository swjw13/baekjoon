from collections import deque
import sys

input = sys.stdin.readline
dydx = [(1, 0), (-1, 0), (0, 1), (0, -1)]

row, col = list(map(int, input().split()))
mp = []
for _ in range(row):
    mp.append(list(map(int, input().split())))

turn = 3

while True:
    queue = deque([(0, 0)])
    mp[0][0] = turn

    while queue:
        current_row, current_col = queue.popleft()
        for (dx, dy) in dydx:
            x = current_row + dx
            y = current_col + dy
            if 0 <= x < row and 0 <= y < col and (mp[x][y] == 0 or mp[x][y] == turn - 1):
                queue.append((x, y))
                mp[x][y] = turn

    after_count = 0
    clipboard = [[False for _ in range(col)] for _ in range(row)]

    for i in range(row):
        for j in range(col):
            if mp[i][j] == 1:
                count_air = 0
                for (dx, dy) in dydx:
                    if mp[i + dx][j + dy] == turn:
                        count_air += 1
                if count_air >= 2:
                    clipboard[i][j] = True
                else:
                    after_count += 1

    if after_count == 0:
        print(turn - 2)
        break
    else:
        for i in range(row):
            for j in range(col):
                if clipboard[i][j]:
                    mp[i][j] = turn
    turn += 1
