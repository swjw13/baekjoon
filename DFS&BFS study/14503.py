import sys

input = sys.stdin.readline

dydx = [(-1, 0), (0, 1), (1, 0), (0, -1)]

count = 0

N, M = list(map(int, input().split()))
r, c, d = list(map(int, input().split()))
room = []
for _ in range(N):
    room.append(list(map(int, input().split())))

stack = [(r, c)]
while True:
    current_row, current_col = stack[-1]

    if room[current_row][current_col] == 0:
        room[current_row][current_col] = 2
        count += 1

    d = (d - 1) % 4
    if room[current_row + dydx[d][0]][current_col + dydx[d][1]] == 0:
        stack[-1] = (current_row + dydx[d][0], current_col + dydx[d][1])
        continue

    d = (d - 1) % 4
    if room[current_row + dydx[d][0]][current_col + dydx[d][1]] == 0:
        stack[-1] = (current_row + dydx[d][0], current_col + dydx[d][1])
        continue

    d = (d - 1) % 4
    if room[current_row + dydx[d][0]][current_col + dydx[d][1]] == 0:
        stack[-1] = (current_row + dydx[d][0], current_col + dydx[d][1])
        continue

    d = (d - 1) % 4
    if room[current_row + dydx[d][0]][current_col + dydx[d][1]] == 0:
        stack[-1] = (current_row + dydx[d][0], current_col + dydx[d][1])
        continue

    if room[current_row + dydx[(d + 2) % 4][0]][current_col + dydx[(d + 2) % 4][1]] == 1:
        print(count)
        break
    else:
        stack[-1] = (current_row + dydx[(d + 2) % 4][0], current_col + dydx[(d + 2) % 4][1])
