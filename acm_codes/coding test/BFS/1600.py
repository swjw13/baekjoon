import sys
from collections import deque

input = sys.stdin.readline
original = [(-1, 0), (1, 0), (0, 1), (0, -1)]
horse_move = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]

K = int(input())
W, H = list(map(int, input().split()))
mp = []
for _ in range(H):
    mp.append(list(map(int, input().split())))

visited = [[[False for _ in range(W)] for _ in range(H)] for _ in range(K + 1)]
queue = deque([(0, 0, K, 0)])
visited[K][0][0] = True
ans = -1

while queue:
    current_row, current_col, ability, turn = queue.popleft()
    if current_row == H - 1 and current_col == W - 1:
        ans = turn
        break

    if ability > 0:
        for (dx, dy) in horse_move:
            x = current_row + dx
            y = current_col + dy

            if 0 <= x < H and 0 <= y < W and not visited[ability - 1][x][y] and mp[x][y] != 1:
                visited[ability - 1][x][y] = True
                queue.append((x, y, ability - 1, turn + 1))

    for (dx, dy) in original:
        x = current_row + dx
        y = current_col + dy

        if 0 <= x < H and 0 <= y < W and not visited[ability][x][y] and mp[x][y] != 1:
            visited[ability][x][y] = True
            queue.append((x, y, ability, turn + 1))

print(ans)