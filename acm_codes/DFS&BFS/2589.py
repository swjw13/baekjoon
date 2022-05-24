import sys
from collections import deque

input = sys.stdin.readline
dydx = [(1, 0), (-1, 0), (0, 1), (0, -1)]

L, W = list(map(int, input().split()))

treasure_map = [["-" for _ in range(W + 2)]]
for _ in range(L):
    tmp = list(input())[:-1]
    treasure_map.append(["-"] + tmp + ["-"])
treasure_map.append(["-" for _ in range(W + 2)])

mx = 0

for i in range(1, L + 1):
    for j in range(1, W + 1):
        if treasure_map[i][j] == "L":
            count_L = 0
            for (dx, dy) in dydx:
                if treasure_map[i + dx][j + dy] == "L":
                    count_L += 1

            # 주변 L의 갯수가 2개 이하인 경우만 BFS를 해줌
            if count_L <= 2:
                visited = [[False for _ in range(W + 2)] for _ in range(L + 2)]
                queue = deque([(i, j, 0)])
                visited[i][j] = True

                dist = 0

                while queue:
                    current_row, current_col, distance = queue.popleft()
                    dist = distance

                    for (dx, dy) in dydx:
                        x = current_row + dx
                        y = current_col + dy
                        if 1 <= x < L + 1 and 1 <= y < W + 1 and not visited[x][y] and treasure_map[x][y] == "L":
                            queue.append((x, y, distance + 1))
                            visited[x][y] = True
                if dist > mx:
                    mx = dist

print(mx)
