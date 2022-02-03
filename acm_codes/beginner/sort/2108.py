import sys

N = int(input())
lst1 = [0 for i in range(8001)]
lst2 = []

total = 0
min = 5000
max = -5000

max_count = 0
max_list = []

for _ in range(N):
    n = int(sys.stdin.readline())
    # 산술평균
    total += n

    # 범위
    if n > max:
        max = n
    if n < min:
        min = n

    # 중앙값
    lst2.append(n)

    # 최빈값
    lst1[n+4000] += 1
    if lst1[n+4000] > max_count:
        max_count = lst1[n+4000]
        max_list = [n]
    elif lst1[n+4000] == max_count:
        max_list.append(n)

lst2.sort()
max_list.sort()

print(round(total/N))
print(lst2[N//2])
if len(max_list) == 1:
    print(max_list[0])
else:
    print(max_list[1])
print(max-min)