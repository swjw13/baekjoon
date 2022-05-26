# https://programmers.co.kr/learn/courses/30/lessons/72415
# 카드 짝 맞추기
from collections import deque, defaultdict
from itertools import permutations
import sys

dxdy = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def solution(board, r, c):
    def find_distance(row, col, target_row, target_col, board_tmp):
        if target_row == row and target_col == col:
            return 0
        visited = [[0 for _ in range(4)] for _ in range(4)]
        queue = deque([(row, col, 0)])
        visited[row][col] = 100000
        while queue:
            cur_row, cur_col, turn = queue.popleft()
            for dx, dy in dxdy:
                new_row = cur_row + dx
                new_col = cur_col + dy
                while 0 <= new_row < 4 and 0 <= new_col < 4 and board_tmp[new_row][new_col] == 0:
                    new_row += dx
                    new_col += dy
                if new_row == 4:
                    if visited[3][new_col] == 0:
                        visited[3][new_col] = turn + 1
                        queue.append((3, new_col, turn + 1))
                elif new_col == 4:
                    if visited[new_row][3] == 0:
                        visited[new_row][3] = turn + 1
                        queue.append((new_row, 3, turn + 1))
                elif new_row == -1:
                    if visited[0][new_col] == 0:
                        visited[0][new_col] = turn + 1
                        queue.append((0, new_col, turn + 1))
                elif new_col == -1:
                    if visited[new_row][0] == 0:
                        visited[new_row][0] = turn + 1
                        queue.append((new_row, 0, turn + 1))
                else:
                    if visited[new_row][new_col] == 0:
                        visited[new_row][new_col] = turn + 1
                        queue.append((new_row, new_col, turn + 1))

                if 0 <= cur_row + dx < 4 and 0 <= cur_col + dy < 4 and visited[cur_row + dx][cur_col + dy] == 0:
                    visited[cur_row + dx][cur_col + dy] = turn + 1
                    queue.append((cur_row + dx, cur_col + dy, turn + 1))
        visited[row][col] = 0
        return visited[target_row][target_col]

    answer = sys.maxsize
    group_dict = defaultdict(list)
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                group_dict[board[i][j]].append((i, j))
    lst = [i for i in group_dict.keys()]
    max_turn = len(lst)

    def loop(ls, cur_turn, max_turn, chosen_number, board_tmp):
        newboard = []
        for i in board_tmp:
            line = []
            for j in i:
                line.append(j)
            newboard.append(line)
        cur_point = group_dict[ls[cur_turn - 1]][chosen_number]
        another_point = group_dict[ls[cur_turn - 1]][chosen_number ^ 1]
        b = find_distance(cur_point[0], cur_point[1], another_point[0], another_point[1], newboard)

        if cur_turn == max_turn:
            return b
        else:
            t1 = find_distance(another_point[0], another_point[1], group_dict[ls[cur_turn]][0][0],
                               group_dict[ls[cur_turn]][0][1], newboard)
            t2 = find_distance(another_point[0], another_point[1], group_dict[ls[cur_turn]][1][0],
                               group_dict[ls[cur_turn]][1][1], newboard)
            for i in group_dict[ls[cur_turn - 1]]:
                newboard[i[0]][i[1]] = 0

            tmp1 = loop(ls, cur_turn + 1, max_turn, 0, newboard) + t1 + b
            tmp2 = loop(ls, cur_turn + 1, max_turn, 1, newboard) + t2 + b
            return min(tmp1, tmp2)

    for i in permutations(lst):
        next = group_dict[i[0]]
        tmp1 = loop(i, 1, max_turn, 0, board) + find_distance(r, c, next[0][0], next[0][1], board)
        tmp2 = loop(i, 1, max_turn, 1, board) + find_distance(r, c, next[1][0], next[1][1], board)
        answer = min(answer, tmp1 + max_turn * 2, tmp2 + max_turn * 2)

    return answer


a = [[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]]

print(solution(a, 1, 0))
