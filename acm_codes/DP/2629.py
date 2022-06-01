# https://www.acmicpc.net/problem/2629
# 양 팔 저울

import sys
input = sys.stdin.readline

N = int(input())
bells = list(map(int, input().split()))
bell_length = len(bells)
T = int(input())
checks = list(map(int, input().split()))

max_value = sum(bells)
visited = [[False for _ in range(max_value + 1)] for _ in range(bell_length + 1)]

visited[0][max_value] = True

for i in range(bell_length):
    for j in range(max_value, 0, -1):
        if visited[i][j]:
            visited[i + 1][j] = True
            if j - bells[i] >= 0:
                visited[i + 1][j - bells[i]] = True
            if j - 2 * bells[i] >= 0:
                visited[i + 1][j - 2 * bells[i]] = True

for tmp in checks:
    if tmp <= max_value and visited[bell_length][tmp]:
        print("Y", end=" ")
    else:
        print("N", end=" ")