# 최소비용으로 주유소 달리기

N = int(input())
km = list(map(int, input().split()))
price = list(map(int, input().split()))

total = 0

min_station = 1000000000
width = len(km)

for i in range(width):
    if price[i] < min_station:
        min_station = price[i]
    total += km[i] * min_station

print(total)