import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))
lst = list(map(int, input().split()))

count = [0 for _ in range(N + 1)]
count[1] = lst[0]
for i in range(2, N + 1):
    count[i] = count[i - 1] + lst[i - 1]

ans = []
for _ in range(M):
    i, j = list(map(int, input().split()))
    ans.append(count[j] - count[i - 1])

for i in ans:
    print(i)