import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    money = int(input())
    count = [0 for _ in range(money + 1)]

    for coin in coins:
        if coin < money + 1:
            count[coin] += 1
            for i in range(coin + 1, money + 1):
                count[i] += count[i - coin]
    print(count[-1])
