# 배열 돌리기
# https://www.acmicpc.net/problem/20327

import sys

input = sys.stdin.readline

N, R = list(map(int, input().split()))
length = int(pow(2, N))
lst = []
for _ in range(length):
    lst.append(list(map(int, input().split())))


def rotation(board, rot_num, l,
             start_row, start_col):
    length_part = int(pow(2, l))
    if rot_num == 1:
        for row in range(length_part // 2):
            for col in range(length_part):
                board[start_row + row][start_col + col], board[start_row + length_part - 1 - row][start_col + col] = \
                    board[start_row + length_part - 1 - row][start_col + col], board[start_row + row][start_col + col]

    elif rot_num == 2:
        for row in range(length_part):
            for col in range(length_part // 2):
                board[start_row + row][start_col + col], board[start_row + row][start_col + length_part - 1 - col] = \
                board[start_row + row][start_col + length_part - 1 - col], board[start_row + row][start_col + col]

    elif rot_num == 3:
        tmp = [[0 for _ in range(length_part)] for _ in range(length_part)]
        start_row = 0
        tmp_length = length_part
        while tmp_length > 1:
            for i in range(tmp_length):
                tmp[start_row + i][tmp_length - start_row] = board[start_row][start_row + i]

            pass
    elif rot_num == 4:
        pass
    elif rot_num == 5:
        pass
    else:
        pass
