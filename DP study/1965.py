import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
ans = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if lst[j] < lst[i]:
            ans[i] = max(ans[i], ans[j] + 1)

print(max(ans))
