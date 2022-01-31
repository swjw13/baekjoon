import sys
from collections import deque

input = sys.stdin.readline
dxdydz = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

while True:
    L, R, C = list(map(int, input().split()))
    if L == 0 and R == 0 and C == 0:
        break
    building = []
    start_point = None
    end_point = None

    for i in range(L):
        one_floor = []
        for j in range(R):
            line = list(input())[:-1]

            if "S" in line:
                tmp = line.index("S")
                start_point = (i, j, tmp)
                line[tmp] = "."
            if "E" in line:
                tmp = line.index("E")
                end_point = (i, j, tmp)
                line[tmp] = "."

            one_floor.append(line)
        building.append(one_floor)
        input()

    queue = deque([(start_point, 0)])

    if_find = -1
    while queue:
        current_point, minute = queue.popleft()
        if current_point == end_point:
            if_find = minute
            break
        for (dx, dy, dz) in dxdydz:
            x = current_point[0] + dx
            y = current_point[1] + dy
            z = current_point[2] + dz
            if 0 <= x < L and 0 <= y < R and 0 <= z < C and building[x][y][z] == ".":
                queue.append(((x, y, z), minute + 1))
                building[x][y][z] = "#"

    if if_find == -1:
        print("Trapped!")
    else:
        print("Escaped in {} minute(s).".format(if_find))
