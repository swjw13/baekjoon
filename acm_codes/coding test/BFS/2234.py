# 성곽
# https://www.acmicpc.net/problem/2234

import sys
from collections import deque

input = sys.stdin.readline
dxdy = {1: (0, -1), 2: (-1, 0), 4: (0, 1), 8: (1, 0)}

N, M = list(map(int, input().split()))
mp = []
for _ in range(M):
    mp.append(list(map(int, input().split())))

room_finding = [[0 for _ in range(N)] for _ in range(M)]
room_num = 1
room_dict = dict()

for i in range(M):
    for j in range(N):
        if room_finding[i][j] == 0:
            queue = deque([(i, j)])
            room_finding[i][j] = room_num
            count = 1
            while queue:
                current_row, current_col = queue.popleft()
                operation = mp[current_row][current_col] ^ 15
                tmp = 1
                while tmp < 16:
                    if (operation & tmp) == tmp:
                        movement = dxdy[tmp]
                        new_row = current_row + movement[0]
                        new_col = current_col + movement[1]
                        if 0 <= new_row < M and 0 <= new_col < N and room_finding[new_row][new_col] == 0:
                            queue.append((new_row, new_col))
                            room_finding[new_row][new_col] = room_num
                            count += 1
                    tmp *= 2

            room_dict[room_num] = count
            room_num += 1

ans_1 = len(room_dict.keys())
ans_2 = max(room_dict.values())
ans_3 = 0
for i in range(M):
    for j in range(N):
        for (dx, dy) in dxdy.values():
            new_row = i + dx
            new_col = j + dy
            if 0 <= new_row < M and 0 <= new_col < N and room_finding[i][j] != room_finding[new_row][new_col]:
                ans_3 = max(ans_3, room_dict[room_finding[i][j]] + room_dict[room_finding[new_row][new_col]])

print(ans_1)
print(ans_2)
print(ans_3)
