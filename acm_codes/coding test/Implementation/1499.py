# 주사위 굴리기
# https://www.acmicpc.net/problem/14499

import sys
from collections import deque

input = sys.stdin.readline

move_by_action = [0, (0, 1), (0, -1), (-1, 0), (1, 0)]
dice_number = [0 for _ in range(6)]
# 해당 index 가 top 이고 명령어 가 들어 왔을 때 head 가 되는 number
# dice_to_index = [[0, 4, 5, 1, 3],
#                  [0, 4, 5, 2, 0],
#                  [0, 4, 5, 3, 1],
#                  [0, 4, 5, 0, 2],
#                  [0, 2, 0, 1, 3],
#                  [0, 0, 2, 1, 3]]
# 해당 index 가 top 일때 bottom 이 되는 index
dice_top_index = 0
dice_bottom_index = 2
dice_side_index = (3, 5, 1, 4)

N, M, x, y, K = list(map(int, input().split()))
mp = []
for _ in range(N):
    mp.append(list(map(int, input().split())))
actions = deque(list(map(int, input().split())))

while actions:
    current_action = actions.popleft()

    # 범위 밖을 벗어 났을 경우 무시
    if not 0 <= x + move_by_action[current_action][0] < N or not 0 <= y + move_by_action[current_action][1] < M:
        continue

    # 이동
    x += move_by_action[current_action][0]
    y += move_by_action[current_action][1]

    # head 변경
    tmp_top = dice_top_index
    tmp_bottom = dice_bottom_index
    if current_action == 1:
        dice_top_index = dice_side_index[3]
        dice_bottom_index = dice_side_index[1]
        dice_side_index = (dice_side_index[0], tmp_top, dice_side_index[2], tmp_bottom)
    elif current_action == 2:
        dice_top_index = dice_side_index[1]
        dice_bottom_index = dice_side_index[3]
        dice_side_index = (dice_side_index[0], tmp_bottom, dice_side_index[2], tmp_top)
    elif current_action == 3:
        dice_top_index = dice_side_index[2]
        dice_bottom_index = dice_side_index[0]
        dice_side_index = (tmp_top, dice_side_index[1], tmp_bottom, dice_side_index[3])
    else:
        dice_top_index = dice_side_index[0]
        dice_bottom_index = dice_side_index[2]
        dice_side_index = (tmp_bottom, dice_side_index[1], tmp_top, dice_side_index[3])

    if mp[x][y] == 0:
        mp[x][y] = dice_number[dice_bottom_index]
    else:
        dice_number[dice_bottom_index] = mp[x][y]
        mp[x][y] = 0

    print(dice_number[dice_top_index])
