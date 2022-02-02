import sys

input = sys.stdin.readline

n = int(input())
grams = list(map(int, input().split()))
grams.sort()
m = min(grams)

k_num = int(input())
ks = list(map(int, input().split()))
k = sum(grams)

dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

i = 0
for gram in grams:
    dp[i][k] = 1
    for q in range(k, -1, -1):
        dp[i + 1][q] = 1
        if dp[i][q] == 1 and q - gram >= 0:
            dp[i + 1][q - gram] = 1
        if dp[i][q] == 1 and q - 2 * gram >= 0:
            dp[i + 1][q - 2 * gram] = 1
    i += 1

for a in ks:
    if dp[i][a] == 1:
        print("Y")
    else:
        print("N")
