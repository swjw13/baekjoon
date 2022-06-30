# https://programmers.co.kr/learn/courses/30/lessons/49994
# 방문 길이

from collections import defaultdict


def solution(dirs):
    answer = 0

    movement = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
    cur_pos = [0, 0]
    visited = defaultdict(bool)

    for i in dirs:

        new_mov = movement[i]
        new_row = cur_pos[0] + new_mov[0]
        new_row = max(min(new_row, 5), -5)
        new_col = cur_pos[1] + new_mov[1]
        new_col = max(min(new_col, 5), -5)
        new_pos = [new_row, new_col]
        if cur_pos != new_pos:
            if not visited[tuple(cur_pos + new_pos)] and not visited[tuple(new_pos + cur_pos)]:
                visited[tuple(cur_pos + new_pos)] = True
                visited[tuple(new_pos + cur_pos)] = True
                answer += 1
        cur_pos = new_pos


    return answer


a = "ULURRDLLU"
print(solution(a))
