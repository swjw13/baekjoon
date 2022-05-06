import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dydx = [(-1, 0), (1, 0), (0, -1), (0, 1)]

T = int(input())
for _ in range(T):
    M, N, K = list(map(int, input().split()))
    board = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        start, end = list(map(int, input().split()))
        board[end][start] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                queue = deque([(i, j)])
                board[i][j] = 0
                while queue:
                    cur_row, cur_col = queue.popleft()
                    for dx, dy in dydx:
                        new_row = cur_row + dx
                        new_col = cur_col + dy
                        if 0 <= new_row < N and 0 <= new_col < M and board[new_row][new_col] == 1:
                            queue.append((new_row, new_col))
                            board[new_row][new_col] = 0
                count += 1


    print(count)
