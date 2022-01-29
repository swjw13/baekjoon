import sys
input = sys.stdin.readline

n, k = list(map(int, input().split()))
coins = [0 for _ in range(k + 1)]

for _ in range(n):
    coin = int(input())
    if coin < k + 1:
        coins[coin] += 1
        for i in range(coin + 1, k + 1):
            if i - coin >= 0:
                coins[i] += coins[i - coin]

print(coins[k])