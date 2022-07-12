# https://www.acmicpc.net/problem/2437
# 저울

N = int(input())
lst = list(map(int, input().split()))

lst.sort()
total = 0
for i in lst:
    if total + 1 < i:
        break
    else:
        total += i
print(total + 1)