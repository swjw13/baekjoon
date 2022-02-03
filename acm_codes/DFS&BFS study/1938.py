# 통나무 옮기기

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

visited = [[[False, False, False] for _ in range(N + 2)] for _ in range(N + 2)]

# 통나무를 옮길 때 체크할 부분을 정의
# index 1: 세로 모양
# index -1: 가로 모양
# 위 아래 왼쪽 오른쪽
checklist_per_position = [[], [[(-2, 0)], [(2, 0)], [(-1, -1), (0, -1), (1, -1)], [(-1, 1), (0, 1), (1, 1)]],
                          [[(-1, -1), (-1, 0), (-1, 1)], [(1, -1), (1, 0), (1, 1)], [(0, -2)], [(0, 2)]]]

# 회전하는 경우에는 오른쪽, 왼쪽 확인 파트를 모두 확인
checklist_rotation = [[], checklist_per_position[1][2] + checklist_per_position[1][3],
                      checklist_per_position[-1][0] + checklist_per_position[-1][1]]

# 맵 주변을 -1로 감싸서 index시에 문제가 생기지 않도록 함
field = [[-1 for _ in range(N + 2)]]

start_middle_check = 0
end_middle_check = 0

start_pos = 0
end_pos = 0
start_point = None
end_point = None

for i in range(N):
    tmp = list(input())[:-1]
    for j in range(N):
        if tmp[j] == "B":
            if start_middle_check == 1:
                start_point = (i + 1, j + 1)
                if j + 1 < N and tmp[j + 1] == "B":
                    start_pos = -1  # 가로 모양
                else:
                    start_pos = 1  # 세로 모양

            start_middle_check += 1
            tmp[j] = "0"

        elif tmp[j] == "E":
            if end_middle_check == 1:
                end_point = (i + 1, j + 1)
                if j + 1 < N and tmp[j + 1] == "E":
                    end_pos = -1  # 가로 모양
                else:
                    end_pos = 1  # 세로 모양
            end_middle_check += 1
            tmp[j] = "0"

    field.append([-1] + list(map(int, tmp)) + [-1])
field.append([-1 for _ in range(N + 2)])

queue = deque([(start_point[0], start_point[1], start_pos, 0)])
visited[start_point[0]][start_point[1]][start_pos] = True

ans = 0

while queue:
    current_row, current_col, current_pos, turn = queue.popleft()

    if current_row == end_point[0] and current_col == end_point[1] and current_pos == end_pos:
        ans = turn
        break

    # 위로 가는 경우
    tmp = True
    for (dx, dy) in checklist_per_position[current_pos][0]:
        if field[current_row + dx][current_col + dy] != 0:
            tmp = False
            break
    if not visited[current_row - 1][current_col][current_pos] and tmp:
        queue.append((current_row - 1, current_col, current_pos, turn + 1))
        visited[current_row - 1][current_col][current_pos] = True

    # 아래로 가는 경우
    tmp = True
    for (dx, dy) in checklist_per_position[current_pos][1]:
        if field[current_row + dx][current_col + dy] != 0:
            tmp = False
            break
    if not visited[current_row + 1][current_col][current_pos] and tmp:
        queue.append((current_row + 1, current_col, current_pos, turn + 1))
        visited[current_row + 1][current_col][current_pos] = True

    # 왼쪽으로 가는 경우
    tmp = True
    for (dx, dy) in checklist_per_position[current_pos][2]:
        if field[current_row + dx][current_col + dy] != 0:
            tmp = False
            break
    if not visited[current_row][current_col - 1][current_pos] and tmp:
        queue.append((current_row, current_col - 1, current_pos, turn + 1))
        visited[current_row][current_col - 1][current_pos] = True

    # 오른쪽으로 가는 경우
    tmp = True
    for (dx, dy) in checklist_per_position[current_pos][3]:
        if field[current_row + dx][current_col + dy] != 0:
            tmp = False
            break
    if not visited[current_row][current_col + 1][current_pos] and tmp:
        queue.append((current_row, current_col + 1, current_pos, turn + 1))
        visited[current_row][current_col + 1][current_pos] = True

    # 회전하는 경우
    tmp = True
    for (dx, dy) in checklist_rotation[current_pos]:
        if field[current_row + dx][current_col + dy] != 0:
            tmp = False
            break
    if not visited[current_row][current_col][current_pos * -1] and tmp:
        queue.append((current_row, current_col, current_pos * -1, turn + 1))
        visited[current_row][current_col][current_pos * -1] = True

print(ans)
