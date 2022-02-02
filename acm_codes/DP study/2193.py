N = int(input())

lst = [1 for i in range(N + 1)]

for i in range(3, N + 1):
    lst[i] = lst[i - 1] + lst[i - 2]

print(lst[N])