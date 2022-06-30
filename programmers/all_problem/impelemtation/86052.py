# https://programmers.co.kr/learn/courses/30/lessons/86052
# 빛의 경로 사이클
from collections import defaultdict

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def solution(grid):
    answer = []
    row_max = len(grid)
    col_max = len(grid[0])
    visited = [[[False for _ in range(4)] for _ in range(col_max)] for _ in range(row_max)]

    def simul(sx, sy, sd):
        x, y, d = sx, sy, sd
        cnt = 0
        visited[sx][sy][sd] = True
        while True:
            x = (x + directions[d][0]) % row_max
            y = (y + directions[d][1]) % col_max
            cnt += 1

            if grid[x][y] == 'R':
                d = (d + 1) % 4
            elif grid[x][y] == 'L':
                d = (d - 1) % 4

            if visited[x][y][d]:
                if (x, y, d) == (sx, sy, sd):
                    return cnt
                else:
                    return 0
            visited[x][y][d] = True

    for i in range(row_max):
        for j in range(col_max):
            for d in range(4):
                res = simul(i, j, d)
                if res != 0:
                    answer.append(res)

    return sorted(answer)
