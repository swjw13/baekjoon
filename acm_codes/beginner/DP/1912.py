# 연속 합
N = int(input())
lst = list(map(int, input().split()))

mx = lst[0]
tmp = lst[0]

for i in range(1, N):
    if lst[i] > mx:
        mx = lst[i]
    if lst[i] >= 0:
        tmp += lst[i]
        if tmp > mx:
            mx = tmp
    else:
        if tmp + lst[i] >= 0:
            tmp += lst[i]
            if tmp > mx:
                mx = tmp
        else:
            tmp = 0

print(mx)
