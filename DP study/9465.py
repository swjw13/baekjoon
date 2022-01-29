import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    stickers = []
    for _ in range(2):
        stickers.append(list(map(int, input().split())))
    dp = [[0 for _ in range(n)] for _ in range(2)]
    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]
    if n != 1:
        dp[0][1] = stickers[0][1] + dp[1][0]
        dp[1][1] = stickers[1][1] + dp[0][0]

        for i in range(2, n):
            before_two = max(dp[0][i - 2], dp[1][i - 2])
            dp[0][i] = max(before_two, dp[1][i - 1]) + stickers[0][i]
            dp[1][i] = max(before_two, dp[0][i - 1]) + stickers[1][i]

    print(max(dp[0][n - 1], dp[1][n - 1]))
