T = int(input())
lst = [1 for i in range(12)]
lst[2] = 2
for i in range(3, 12):
    lst[i] = lst[i - 1] + lst[i - 2] + lst[i - 3]
for _ in range(T):
    num = int(input())
    print(lst[num])
