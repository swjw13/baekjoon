import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dydx = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(row, col, mp, N, M):
    mp[row][col] = 0
    for (dy, dx) in dydx:
        x = row + dy
        y = col + dx
        if 0 <= x < N and 0 <= y < M and mp[x][y] == 1:
            dfs(x, y, mp, N, M)


T = int(input())
for _ in range(T):
    lines = []
    M, N, K = list(map(int, input().split()))
    m = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        start, end = list(map(int, input().split()))
        m[end][start] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            if m[i][j] == 1:
                dfs(i, j, m, N, M)
                count += 1
    print(count)
