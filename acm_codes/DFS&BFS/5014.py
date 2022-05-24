import sys
from collections import deque

input = sys.stdin.readline

max_floor, start_floor, end_floor, up, down = list(map(int, input().split()))

visited = [False for _ in range(max_floor + 1)]
queue = deque([(start_floor, 0)])
visited[start_floor] = True

ans = -1

while queue:
    current_floor, count = queue.popleft()
    if current_floor == end_floor:
        ans = count
        break
    stair_up = current_floor + up
    stair_down = current_floor - down

    if stair_up <= max_floor and not visited[stair_up]:
        queue.append((stair_up, count + 1))
        visited[stair_up] = True
    if stair_down >= 1 and not visited[stair_down]:
        queue.append((stair_down, count + 1))
        visited[stair_down] = True

if ans == -1:
    print("use the stairs")
else:
    print(ans)