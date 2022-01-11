import sys

board = []
zeros = []
for i in range(9):
    line = list(map(int, sys.stdin.readline().split()))
    board.append(line)
    for k in range(9):
        if line[k] == 0:
            zeros.append((i, k))

num_zero = len(zeros)


def able(row, col, value):
    if value in board[row]:
        return False
    for i in range(9):
        if board[i][col] == value:
            return False
    for i in range(3):
        for j in range(3):
            if board[i + (row // 3) * 3][j + (col // 3) * 3] == value:
                return False
    return True


def all_zero():
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return False
    return True


def check(stack):
    if stack == num_zero:
        if all_zero():
            for line in board:
                for point in line:
                    print(point, end=' ')
                print()
            sys.exit()
    else:
        for value in range(1, 10):
            if able(zeros[stack][0], zeros[stack][1], value):
                board[zeros[stack][0]][zeros[stack][1]] = value
                check(stack + 1)
                board[zeros[stack][0]][zeros[stack][1]] = 0


check(0)
