# 경사로
# https://www.acmicpc.net/problem/14890
# 반례에 대해 생각해 볼 수 있어야 한다.,,,

import sys

input = sys.stdin.readline

N, L = list(map(int, input().split()))
mp = []
for _ in range(N):
    mp.append(list(map(int, input().split())))

total = 0

# 각 row 체크하기
for i in range(N):
    tmp = True
    turn = 1
    prev = 0
    for j in range(N - 1):
        if prev == 1 and turn == L:
            prev = 0
            turn = 0

        if mp[i][j] == mp[i][j + 1]:
            turn += 1
        elif mp[i][j] > mp[i][j + 1]:
            if mp[i][j] - mp[i][j + 1] != 1:
                tmp = False
                break
            if prev == 1:
                tmp = False
                break
            prev = 1
            turn = 1
        else:
            if mp[i][j] - mp[i][j + 1] != -1:
                tmp = False
                break
            if prev == 1:
                tmp = False
                break
            else:
                if turn < L:
                    tmp = False
                    break
                else:
                    turn = 1
    if prev == 1:
        if turn < L:
            tmp = False

    if tmp:
        # print("row: {}".format(i))
        total += 1

# row 에 대해서 진행
for j in range(N):
    tmp = True
    turn = 1
    prev = 0
    for i in range(N - 1):
        if prev == 1 and turn == L:
            prev = 0
            turn = 0

        if mp[i][j] == mp[i + 1][j]:
            turn += 1
        elif mp[i][j] > mp[i + 1][j]:
            if mp[i][j] - mp[i + 1][j] != 1:
                tmp = False
                break
            if prev == 1:
                tmp = False
                break
            else:
                prev = 1
                turn = 1
        else:
            if mp[i][j] - mp[i + 1][j] != -1:
                tmp = False
                break
            if prev == 1:
                tmp = False
                break
            else:
                if turn < L:
                    tmp = False
                    break
                else:
                    turn = 1
    if prev == 1:
        if turn < L:
            tmp = False

    if tmp:
        # print("col: {}".format(j))
        total += 1

print(total)
