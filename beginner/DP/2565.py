# 전깃줄 문제

N = int(input())
lines = []
for _ in range(N):
    num1, num2 = list(map(int, input().split()))
    lines.append((num1, num2))

lines.sort(key=lambda x: x[0])
ans = [1 for i in range(N)]
for i in range(1, N):
    for j in range(i):
        if lines[j][1] < lines[i][1]:
            ans[i] = max(ans[j] + 1, ans[i])

print(N - max(ans))
