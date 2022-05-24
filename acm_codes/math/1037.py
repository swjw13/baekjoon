# 진짜 약수

N = int(input())
lst = list(map(int, input().split()))

lst.sort()
print(lst[0] * lst[-1])