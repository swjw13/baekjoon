N = int(input())
lst = list(map(int, input().split()))
count = [i for i in lst]

for i in range(1, N):
    for j in range(i):
        if lst[j] < lst[i]:
            count[i] = max(count[i], count[j] + lst[i])

print(max(count))
