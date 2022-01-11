# LIS(가장 긴 증가 하는 수열)

N = int(input())
lst = list(map(int, input().split()))

ans = [1 for i in range(N)]
for i in range(1, N):
    for j in range(0,i):
        if lst[j] < lst[i]:
            ans[i] = max(ans[j] + 1, ans[i])

print(max(ans))