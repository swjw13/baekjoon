import sys

input = sys.stdin.readline
INF = 1e7

T = int(input())

for _ in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    dp = [[[INF, INF] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        dp[i][i] = [lst[i], 0]

    for column in range(1, N):
        for row in range(column - 1, -1, -1):
            for k in range(row, column):
                x1, w1 = dp[row][k]
                x2, w2 = dp[k + 1][column]

                cost = w1 + w2 + x1 + x2
                if dp[row][column][1] > cost:
                    dp[row][column] = [x1 + x2, cost]

    print(dp[0][N - 1][1])
