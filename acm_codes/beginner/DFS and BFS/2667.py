import sys

input = sys.stdin.readline
houses = []

N = int(input())
for _ in range(N):
    line = list(input())
    houses.append(list(map(int, line[:-1])))

dydx = [(-1, 0), (1, 0), (0, -1), (0, 1)]

count = 0


def dfs(row, col):
    global count
    houses[row][col] = 0
    count += 1
    for (dy, dx) in dydx:
        x = row + dy
        y = col + dx
        if 0 <= x < N and 0 <= y < N and houses[x][y] == 1:
            dfs(x, y)


total = 0
c = []
for i in range(N):
    for j in range(N):
        if houses[i][j] == 1:
            count = 0
            dfs(i, j)
            c.append(count)
            total += 1

c.sort()
print(total)
for i in c:
    print(i)
