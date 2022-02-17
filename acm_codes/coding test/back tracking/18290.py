# NM과 K
# https://www.acmicpc.net/problem/18290

import sys

input = sys.stdin.readline

N, M, K = list(map(int, input().split()))
mp = []
for _ in range(N):
    mp += list(map(int, input().split()))
visited = [False for _ in range(N * M)]
mx = -sys.maxsize


def find_max_total(turn, index, total):
    global mx
    if turn == K:
        mx = max(mx, total)
    elif index < M * N:
        if not visited[index]:
            check_right = False
            if index + 1 < M * N and not visited[index + 1] and (index + 1) % M != 0:
                visited[index + 1] = True
                check_right = True
            check_under = False
            if index + M < M * N and not visited[index + M]:
                visited[index + M] = True
                check_under = True

            find_max_total(turn + 1, index + 1, total + mp[index])

            if index + 1 < M * N and check_right:
                visited[index + 1] = False
            if index + M < M * N and check_under:
                visited[index + M] = False

        find_max_total(turn, index + 1, total)


find_max_total(0, 0, 0)
print(mx)
