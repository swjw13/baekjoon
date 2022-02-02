import sys

input = sys.stdin.readline

M, N = list(map(int, input().split()))
mp = []
visited = []
dp = []
for _ in range(M):
    lst = list(map(int, input().split()))
    mp.append(lst)
    visited.append([False] * N)
    dp.append([0] * N)

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

total = 0


def dfs(graph, i, j):
    global total
    if i == M - 1 and j == N - 1:
        return 1
    if visited[i][j]:
        return dp[i][j]
    else:
        for (dx, dy) in d:
            if M > i + dx >= 0 and N > j + dy >= 0:
                if mp[i][j] > mp[i + dx][j + dy]:
                    dp[i][j] += dfs(graph, i + dx, j + dy)
        visited[i][j] = True

    return dp[i][j]


print(dfs(mp, 0, 0))
