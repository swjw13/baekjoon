lst = [1 for i in range(101)]
lst[4] = 2
lst[5] = 2
for i in range(6,101):
    lst[i] = lst[i-1] + lst[i-5]

T = int(input())
for i in range(T):
    n = int(input())
    print(lst[n])