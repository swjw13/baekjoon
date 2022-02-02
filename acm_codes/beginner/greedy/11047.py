# 동전 갯수

N, K = list(map(int, input().split()))

coins = []
for _ in range(N):
    coin = int(input())
    coins.append(coin)
total = 0
for i in range(N-1,-1,-1):
    total += K // coins[i]
    K = K % coins[i]

print(total)