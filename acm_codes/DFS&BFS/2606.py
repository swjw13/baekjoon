import sys

input = sys.stdin.readline

N = int(input())
visited = [False for _ in range(N + 1)]
network = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

l = int(input())
for _ in range(l):
    start, end = list(map(int, input().split()))
    network[start][end] = 1
    network[end][start] = 1

count = 0


def dfs(s):
    global count
    visited[s] = True
    count += 1
    for i in range(N + 1):
        if network[s][i] == 1 and not visited[i]:
            dfs(i)


dfs(1)
print(count - 1)
