N, M = list(map(int, input().split()))

ans = set()
for _ in range(N):
    ans.add(input())
count = 0
for _ in range(M):
    word = input()
    if word in ans:
        count += 1

print(count)