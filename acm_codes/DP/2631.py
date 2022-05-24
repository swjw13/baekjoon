import sys

input = sys.stdin.readline

N = int(input())
lst = []
ans = [1 for _ in range(N)]
for i in range(N):
    lst.append(int(input()))
    for j in range(i):
        if lst[j] < lst[i]:
            ans[i] = max(ans[i], ans[j] + 1)

print(N - max(ans))
