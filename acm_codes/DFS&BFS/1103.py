# 게임
# https://www.acmicpc.net/problem/1103

import sys
from collections import deque

input = sys.stdin.readline

dxdy = [(-1, 0), (1, 0), (0, 1), (0, -1)]

N, M = list(map(int, input().split()))
board = []
for _ in range(N):
    board.append(list(input().strip()))

visited = [[False for _ in range(M)] for _ in range(N)]

stack = [(0, 0, 0)]
