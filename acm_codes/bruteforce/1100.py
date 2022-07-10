# https://www.acmicpc.net/problem/1100
# 하얀 칸

board = []
for _ in range(8):
    board.append(input())
cnt = 0
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0 and board[i][j] == "F":
            cnt += 1
print(cnt)