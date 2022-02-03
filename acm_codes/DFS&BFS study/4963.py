import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
dydx = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def dfs(mp, row, col, r_max, c_max):
    mp[row][col] = 0
    for (dx, dy) in dydx:
        x = row + dx
        y = col + dy
        if 0 <= x < r_max and 0 <= y < c_max and mp[x][y] == 1:
            dfs(mp, x, y, r_max, c_max)


while True:
    w, h = list(map(int, input().split()))
    if w == 0 and h == 0:
        break
    world = []
    for _ in range(h):
        world.append(list(map(int, input().split())))

    count = 0
    for i in range(h):
        for j in range(w):
            if world[i][j] == 1:
                dfs(world, i, j, h, w)
                count += 1

    print(count)
