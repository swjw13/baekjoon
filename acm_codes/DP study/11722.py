N = int(input())
lst = list(map(int, input().split()))
ans = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if lst[j] > lst[i]:
            ans[i] = max(ans[i], ans[j] + 1)

print(max(ans))