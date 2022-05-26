# https://www.acmicpc.net/problem/24444
# bfs

import sys
from collections import deque, defaultdict
input = sys.stdin.readline

N, M, S = list(map(int, input().split()))
connected = defaultdict(list)
for _ in range(M):
    p1, p2 = list(map(int, input().split()))
    connected[p1].append(p2)
    connected[p2].append(p1)

for i in connected.keys():
    connected[i].sort()

visited = [False for _ in range(N + 1)]
visited[S] = True
queue = deque([S])

ans = defaultdict(int)
ans[S] = 1
count = 2

while queue:
    cur_point = queue.popleft()
    for i in connected[cur_point]:
        if not visited[i]:
            visited[i] = True
            ans[i] = count
            count += 1
            queue.append(i)

for i in range(1, N + 1):
    print(ans[i])

