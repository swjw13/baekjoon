# https://www.acmicpc.net/problem/24479
# dfs

import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N, M, s = list(map(int, input().split()))
connected = defaultdict(list)
for _ in range(M):
    p1, p2 = list(map(int, input().split()))
    connected[p1].append(p2)
    connected[p2].append(p1)

for i in connected.keys():
    connected[i].sort()

visited = [False for _ in range(N + 1)]
visited[s] = True
ans = defaultdict(int)
count = 1
ans[s] = count
count += 1

def dfs(cur_point):
    global count
    for i in connected[cur_point]:
        if not visited[i]:
            visited[i] = True
            ans[i] = count
            count += 1
            dfs(i)

dfs(s)
for i in range(1, N + 1):
    print(ans[i])