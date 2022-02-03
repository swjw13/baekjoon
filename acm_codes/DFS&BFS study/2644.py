import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
answer = -1

N = int(input())
start, end = list(map(int, input().split()))

m = int(input())

lines = [[] for _ in range(N + 1)]
for _ in range(m):
    s, e = list(map(int, input().split()))
    lines[s].append(e)
    lines[e].append(s)

visited = [False for _ in range(N + 1)]
queue = deque([(start, 0)])
visited[start] = True

while queue:
    current_point, dist = queue.popleft()
    if current_point == end:
        answer = dist
        break

    for related_point in lines[current_point]:
        if not visited[related_point]:
            queue.append((related_point, dist + 1))
            visited[related_point] = True

print(answer)
