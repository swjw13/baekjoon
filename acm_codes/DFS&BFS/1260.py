import sys
from collections import deque

input = sys.stdin.readline

N, M, V = list(map(int, input().split()))
lines = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
visited_dfs = [False for _ in range(N + 1)]
visited_bfs = [False for _ in range(N + 1)]
for _ in range(M):
    start, end = list(map(int, input().split()))
    lines[start][end] = 1
    lines[end][start] = 1


def dfs(s):
    visited_dfs[s] = True
    print(s, end=' ')
    for i in range(1, N + 1):
        if lines[s][i] == 1 and not visited_dfs[i]:
            dfs(i)


def bfs(s):
    queue = deque([s])
    visited_bfs[s] = True
    while queue:
        point = queue.popleft()
        print(point, end=' ')
        for i in range(1, N + 1):
            if lines[point][i] == 1 and not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True


dfs(V)
print()
bfs(V)
