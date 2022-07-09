# https://www.acmicpc.net/problem/12100
# 2048게임

import sys

input = sys.stdin.readline

N = int(input())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))


def move_up(lst):
    new_lst = [[[0, 0] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_lst[i][j][0] = lst[i][j]
    for i in range(N):
        for j in range(N):
            row = i
            col = j
            while row - 1 >= 0 and new_lst[row - 1][col][0] == 0:
                new_lst[row - 1][col][0] = new_lst[row][col][0]
                new_lst[row][col][0] = 0
                row -= 1
            if row - 1 >= 0:
                if new_lst[row - 1][col][1] == 0 and new_lst[row - 1][col][0] == new_lst[row][col][0]:
                    new_lst[row - 1][col][0] *= 2
                    new_lst[row - 1][col][1] = 1
                    new_lst[row][col] = [0, 0]

    ans = [[new_lst[i][j][0] for j in range(N)] for i in range(N)]
    return ans


def move_down(lst):
    new_lst = [[[0,0] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_lst[i][j][0] = lst[i][j]
    for i in range(N - 1, -1, -1):
        for j in range(N):
            row = i
            col = j
            while row + 1 < N and new_lst[row + 1][col][0] == 0:
                new_lst[row + 1][col][0] = new_lst[row][col][0]
                new_lst[row][col][0] = 0
                row += 1
            if row + 1 < N:
                if new_lst[row + 1][col][1] == 0 and new_lst[row + 1][col][0] == new_lst[row][col][0]:
                    new_lst[row + 1][col][0] *= 2
                    new_lst[row + 1][col][1] = 1
                    new_lst[row][col] = [0, 0]
    ans = [[new_lst[i][j][0] for j in range(N)] for i in range(N)]
    return ans


def move_left(lst):
    new_lst = [[[0, 0] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_lst[i][j][0] = lst[i][j]
    for j in range(N):
        for i in range(N):
            row = i
            col = j
            while col - 1 >= 0 and new_lst[row][col - 1][0] == 0:
                new_lst[row][col - 1][0] = new_lst[row][col][0]
                new_lst[row][col][0] = 0
                col -= 1
            if col - 1 >= 0:
                if new_lst[row][col - 1][1] == 0 and new_lst[row][col - 1][0] == new_lst[row][col][0]:
                    new_lst[row][col - 1][0] *= 2
                    new_lst[row][col - 1][1] = 1
                    new_lst[row][col] = [0, 0]
    ans = [[new_lst[i][j][0] for j in range(N)] for i in range(N)]
    return ans


def move_right(lst):
    new_lst = [[[0, 0] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_lst[i][j][0] = lst[i][j]
    for j in range(N - 1, -1, -1):
        for i in range(N):
            row = i
            col = j
            while col + 1 < N and new_lst[row][col + 1][0] == 0:
                new_lst[row][col + 1][0] = new_lst[row][col][0]
                new_lst[row][col][0] = 0
                col += 1
            if col + 1 < N:
                if new_lst[row][col + 1][1] == 0 and new_lst[row][col + 1][0] == new_lst[row][col][0]:
                    new_lst[row][col + 1][0] *= 2
                    new_lst[row][col + 1][1] = 1
                    new_lst[row][col] = [0, 0]
    ans = [[new_lst[i][j][0] for j in range(N)] for i in range(N)]
    return ans


def movement(t, lst):
    if t == 0:
        return move_up(lst)
    elif t == 1:
        return move_down(lst)
    elif t == 2:
        return move_left(lst)
    else:
        return move_right(lst)


def get_max(lst):
    answer = 0
    for i in range(N):
        for j in range(N):
            answer = max(answer, lst[i][j])
    return answer


max_value = 0


def game(b, turn):
    global max_value
    # if turn == 1:
    #     print(turn)
    #     print(b)
    max_value = max(max_value, get_max(b))
    if turn < 5:
        for i in range(4):
            game(movement(i, b), turn + 1)


game(board, 0)
print(max_value)
