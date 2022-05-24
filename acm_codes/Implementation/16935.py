# 배열 돌리기
# https://www.acmicpc.net/problem/16935

import sys

input = sys.stdin.readline

N, M, R = list(map(int, input().split()))
mp = []
for _ in range(N):
    mp.append(list(map(int, input().split())))


def action_one():
    for i in range(N // 2):
        mp[i], mp[N - 1 - i] = mp[N - 1 - i], mp[i]


def action_two():
    for i in range(N):
        for j in range(M // 2):
            mp[i][j], mp[i][M - j - 1] = mp[i][M - j - 1], mp[i][j]


def action_three():
    global N, M
    global mp
    tmp = [[0 for _ in range(N)] for _ in range(M)]
    for i in range(N):
        for j in range(M):
            tmp[j][N - 1 - i] = mp[i][j]
    mp = tmp
    N, M = M, N


def action_four():
    global N, M
    global mp
    tmp = [[0 for _ in range(N)] for _ in range(M)]
    for i in range(N):
        for j in range(M):
            tmp[M - 1 - j][i] = mp[i][j]
    mp = tmp
    N, M = M, N


def action_five():
    global mp
    tmp1 = []
    tmp2 = []
    for i in range(N // 2):
        line1 = mp[i]
        line2 = mp[i + N // 2]

        tmp1.append(line2[:M // 2] + line1[:M // 2])
        tmp2.append(line2[M // 2:] + line1[M // 2:])
    mp = tmp1 + tmp2


def action_six():
    global mp
    tmp1 = []
    tmp2 = []
    for i in range(N // 2):
        line1 = mp[i]
        line2 = mp[i + N // 2]

        tmp1.append(line1[M // 2:] + line2[M // 2:])
        tmp2.append(line1[:M // 2] + line2[:M // 2])

    mp = tmp1 + tmp2


actions = [0, action_one, action_two, action_three, action_four, action_five, action_six]

action = list(map(int, input().split()))
for a in action:
    actions[a]()
for i in range(N):
    for j in range(M):
        print(mp[i][j], end=' ')
    print()
