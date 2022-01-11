# ATM 기다리는 시간의 최솟값

N = int(input())
lst = list(map(int, input().split()))

lst.sort()
total = 0
for i in range(N):
    total += lst[i] * (N - i)
print(total)