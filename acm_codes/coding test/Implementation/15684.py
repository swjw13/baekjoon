# 사다리타기
# https://www.acmicpc.net/problem/15684

import sys

input = sys.stdin.readline

N, M, H = list(map(int, input().split()))
lines = [[i for i in range(N)] for _ in range(H)]

for _ in range(M):
    a, b = list(map(int, input().split()))
    lines[a - 1][b - 1] = b
    lines[a - 1][b] = b - 1


def get_result(start_num):
    index_result = start_num
    for i in range(H):
        index_result = lines[i][index_result]
    return index_result


ans = sys.maxsize


def action(added_line_num, row, col):
    global ans

    if added_line_num > 3:
        return
    else:
        tmp = 0
        for i in range(N):
            if i == get_result(i):
                tmp += 1
        if tmp == N:
            ans = min(ans, added_line_num)

        for i in range(col, N - 1):
            if_available = False
            if lines[row][i] == i and lines[row][i + 1] == i + 1:
                if_available = True

            if if_available:
                lines[row][i] = i + 1
                lines[row][i + 1] = i

                action(added_line_num + 1, row, col + 1)

                lines[row][i] = i
                lines[row][i + 1] = i + 1

        for j in range(row + 1, H):
            for i in range(N - 1):
                if_available = False
                if lines[j][i] == i and lines[j][i + 1] == i + 1:
                    if_available = True

                if if_available:
                    lines[j][i] = i + 1
                    lines[j][i + 1] = i

                    action(added_line_num + 1, j, col + 1)

                    lines[j][i] = i
                    lines[j][i + 1] = i + 1


action(0, 0, 0)

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)
