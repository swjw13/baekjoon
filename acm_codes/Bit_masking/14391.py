# 2차원 비트마스크
# https://www.acmicpc.net/problem/14391

import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))
mp = []
for _ in range(N):
    mp.append(list(input())[:-1])

mask = [[1 for _ in range(M)] for _ in range(N)]
tmp = []
ans = []

mx = 0


def masking(turn):
    global mx
    if turn == N * M:
        main_action()
        a = 0
        for i in range(N):
            for j in range(M):
                if ans[i][j]:
                    a += int(tmp[i][j])
        if mx < a:
            mx = a

    else:
        # 백트래킹
        mask[turn // M][turn % M] = 2
        masking(turn + 1)
        mask[turn // M][turn % M] = 1
        masking(turn + 1)

#중점은 각 점이 오른쪽과 연관되느냐, 아래쪽과 연관되느냐 에 있다.
# 오른쪽 값과 연관되는 경우(현재 위치의 수가 가로형 박스 안에 있을 때)
# 만약 row - 1 의 방향이 세로형일 경우 해당 위치의 숫자가 시작일 것이다
# 만약 row + 1 의 방향이 세로형일 경우 해당 위치의 숫자가 마지막일 것이다.
# 현재 위치가 세로일 경우도 비슷한 방법으로 측정하여
# 마지막 위치에서 발견된 연속된 숫자들의 합을 구한다.
def main_action():
    global tmp
    global ans
    ans = [[False for _ in range(M)] for _ in range(N)]
    tmp = [["" for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if i == 0:
                if j == 0:
                    tmp[i][j] = mp[i][j]
                    if mask[i][j] == 1:
                        if j + 1 < M:
                            if mask[i][j + 1] == 2:
                                ans[i][j] = True
                        else:
                            ans[i][j] = True
                    else:
                        if i + 1 < N:
                            if mask[i + 1][j] == 1:
                                ans[i][j] = True
                        else:
                            ans[i][j] = True
                elif j == M - 1:
                    if mask[i][j] == 2:
                        tmp[i][j] = mp[i][j]
                        if i + 1 < N:
                            if mask[i + 1][j] == 1:
                                ans[i][j] = True
                        else:
                            ans[i][j] = True

                    else:
                        if mask[i][j - 1] == 1:
                            tmp[i][j] = tmp[i][j - 1] + mp[i][j]
                            ans[i][j] = True
                        else:
                            tmp[i][j] = mp[i][j]
                            ans[i][j] = True
                else:
                    if mask[i][j] == 2:
                        tmp[i][j] = mp[i][j]

                        if i + 1 < N:
                            if mask[i + 1][j] == 1:
                                ans[i][j] = True
                        else:
                            ans[i][j] = True
                    else:
                        if mask[i][j - 1] == 2:
                            tmp[i][j] = mp[i][j]
                        else:
                            tmp[i][j] = tmp[i][j - 1] + mp[i][j]
                        if mask[i][j + 1] == 2:
                            ans[i][j] = True

            elif i == N - 1:
                if j == 0:
                    if mask[i][j] == 1:
                        tmp[i][j] = mp[i][j]
                        if j + 1 < M:
                            if mask[i][j + 1] == 2:
                                ans[i][j] = True
                        else:
                            ans[i][j] = True

                    else:
                        ans[i][j] = True
                        if mask[i - 1][j] == 1:
                            tmp[i][j] = mp[i][j]
                        else:
                            tmp[i][j] = tmp[i - 1][j] + mp[i][j]

                elif j == M - 1:
                    ans[i][j] = True
                    if mask[i][j] == 1:
                        if mask[i][j - 1] == 2:
                            tmp[i][j] = mp[i][j]
                        else:
                            tmp[i][j] = tmp[i][j - 1] + mp[i][j]
                    else:
                        if mask[i - 1][j] == 1:
                            tmp[i][j] = mp[i][j]
                        else:
                            tmp[i][j] = tmp[i - 1][j] + mp[i][j]

                else:
                    if mask[i][j] == 2:
                        ans[i][j] = True
                        if mask[i - 1][j] == 1:
                            tmp[i][j] = mp[i][j]
                        else:
                            tmp[i][j] = tmp[i - 1][j] + mp[i][j]
                    else:
                        if mask[i][j - 1] == 1:
                            tmp[i][j] = tmp[i][j - 1] + mp[i][j]
                        else:
                            tmp[i][j] = mp[i][j]

                        if mask[i][j + 1] == 2:
                            ans[i][j] = True
            else:
                if j == 0:
                    if mask[i][j] == 1:
                        tmp[i][j] = mp[i][j]
                        if j + 1 < M:
                            if mask[i][j + 1] == 2:
                                ans[i][j] = True
                        else:
                            ans[i][j] = True

                    else:
                        if mask[i - 1][j] == 1:
                            tmp[i][j] = mp[i][j]
                        else:
                            tmp[i][j] = tmp[i - 1][j] + mp[i][j]

                        if mask[i + 1][j] == 1:
                            ans[i][j] = True

                elif j == M - 1:
                    if mask[i][j] == 1:
                        ans[i][j] = True
                        if mask[i][j - 1] == 1:
                            tmp[i][j] = tmp[i][j - 1] + mp[i][j]
                        else:
                            tmp[i][j] = mp[i][j]
                    else:
                        if mask[i - 1][j] == 2:
                            tmp[i][j] = tmp[i - 1][j] + mp[i][j]
                        else:
                            tmp[i][j] = mp[i][j]

                        if mask[i + 1][j] == 1:
                            ans[i][j] = True
                else:
                    if mask[i][j] == 1:
                        if mask[i][j - 1] == 1:
                            tmp[i][j] = tmp[i][j - 1] + mp[i][j]
                        else:
                            tmp[i][j] = mp[i][j]

                        if mask[i][j + 1] == 2:
                            ans[i][j] = True
                    else:
                        if mask[i - 1][j] == 1:
                            tmp[i][j] = mp[i][j]
                        else:
                            tmp[i][j] = tmp[i - 1][j] + mp[i][j]

                        if mask[i + 1][j] == 1:
                            ans[i][j] = True


masking(0)
print(mx)
