import sys

lst = [1 for i in range(1000001)]
for i in range(2,1000001):
    lst[i] = (lst[i-1] + lst[i-2]) % 15746

N = int(sys.stdin.readline())
print(lst[N])