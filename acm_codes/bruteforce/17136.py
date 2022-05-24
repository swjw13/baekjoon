# 색종이 붙이기
# https://www.acmicpc.net/problem/17136

import sys

input = sys.stdin.readline

board = []
for _ in range(10):
    board.append(list(map(int, input().split())))
paper_list = [5 for _ in range(6)]


def checking(row, col, size):
    if row + size - 1 > 9 or col + size - 1 > 9:
        return False
    for i in range(size):
        for j in range(size):
            if board[row + i][col + j] == 0:
                return False
    return True


def swapping(row, col, size, num):
    for i in range(size):
        for j in range(size):
            board[row + i][col + j] = num


mn = sys.maxsize


def action(row, col, count):
    def next_action(new_count):
        if col == 9:
            action(row + 1, 0, new_count)
        else:
            action(row, col + 1, new_count)

    if row == 10:
        global mn
        mn = min(mn, count)

    else:
        if board[row][col] == 0:
            next_action(count)
        else:
            for i in range(1, 6):
                if checking(row, col, i):
                    if paper_list[i] != 0:
                        paper_list[i] -= 1
                        swapping(row, col, i, 0)

                        next_action(count + 1)

                        paper_list[i] += 1
                        swapping(row, col, i, 1)


action(0, 0, 0)
if mn == sys.maxsize:
    print(-1)
else:
    print(mn)
