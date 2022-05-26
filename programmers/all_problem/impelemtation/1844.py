# https://programmers.co.kr/learn/courses/30/lessons/1844
# 게임 맵 최단거리

from collections import deque

dxdy = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def solution(maps):
    answer = -1
    row = len(maps)
    col = len(maps[0])

    visited = [[False for _ in range(col)] for _ in range(row)]

    queue = deque([(0, 0, 1)])
    visited[0][0] = True
    while queue:
        cur_row, cur_col, count = queue.popleft()
        if cur_row == row - 1 and cur_col == col - 1:
            answer = count
            break

        for dx, dy in dxdy:
            new_row = cur_row + dx
            new_col = cur_col + dy
            if 0 <= new_row < row and 0 <= new_col < col and maps[new_row][new_col] == 1 and not visited[new_row][
                new_col]:
                visited[new_row][new_col] = True
                queue.append((new_row, new_col, count + 1))

    return answer
