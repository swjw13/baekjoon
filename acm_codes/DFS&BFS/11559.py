from collections import deque
import sys

input = sys.stdin.readline
dydx = [(1, 0), (-1, 0), (0, 1), (0, -1)]

mp = [deque(), deque(), deque(), deque(), deque(), deque()]

for _ in range(12):
    tmp = list(input())[:-1]
    for i in range(6):
        mp[i].append(tmp[i])

related_bomb = 0
turn = 0

while True:
    count_puyo = 0
    points_to_delete = set()
    visited = [[False for _ in range(12)] for _ in range(6)]

    for i in range(6):
        for j in range(12):
            if mp[i][j] != "." and not visited[i][j]:
                have_to_crash = 1
                letter = mp[i][j]
                queue = deque([(i, j)])
                visited[i][j] = True
                points = [(i, j)]
                while queue:
                    current_row, current_col = queue.popleft()
                    for (dx, dy) in dydx:
                        x = current_row + dx
                        y = current_col + dy
                        if 0 <= x < 6 and 0 <= y < 12 and not visited[x][y] and mp[x][y] == letter:
                            queue.append((x, y))
                            visited[x][y] = True
                            have_to_crash += 1
                            points.append((x, y))

                if have_to_crash >= 4:
                    count_puyo += 1
                    points_to_delete.update(points)
    if count_puyo == 0:
        print(turn)
        break
    else:
        # 위의 점부터 없애면 del 에 의한 index 혼란이 오지 않으므로 위에서 부터 없앤다.
        points_to_delete = list(points_to_delete)
        points_to_delete.sort(key=lambda x: x[1])
        for (x, y) in points_to_delete:
            del mp[x][y]
            mp[x].appendleft(".")
        turn += 1
