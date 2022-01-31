import sys

input = sys.stdin.readline
INF = 1e9

N = int(input())
mats = []
dp = [[[INF, INF, INF] for _ in range(N)] for _ in range(N)]

for i in range(N):
    x, y = list(map(int, input().split()))
    mats.append((x, y))

    dp[i][i] = [x, y, 0]

for column in range(1, N):
    for row in range(column - 1, -1, -1):
        for k in range(row, column):
            x1, y1, w1 = dp[row][k]
            x2, y2, w2 = dp[k + 1][column]

            # y1과 x가 같다는 전제 하에
            cost = w1 + w2 + x1 * x2 * y2
            if dp[row][column][2] > cost:
                dp[row][column] = [x1, y2, cost]

print(dp[0][N - 1][2])
