import sys
from collections import deque
input = sys.stdin.readline

N, M = list(map(int, input().split()))
visited = [False for _ in range(N + 1)]
lines = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end = list(map(int, input().split()))
    lines[start].append(end)
    lines[end].append(start)

count = 0
for i in range(1, N + 1):
    if not visited[i]:
        queue = deque([i])
        visited[i] = True

        while queue:
            current_point = queue.popleft()
            for connected_point in lines[current_point]:
                if not visited[connected_point]:
                    queue.append(connected_point)
                    visited[connected_point] = True
        count += 1

print(count)