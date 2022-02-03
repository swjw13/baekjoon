# 1 6 12 18 24 ...

total = -1
tmp = 1
i = 1
N = int(input())
if N == 1:
    total = 1
else:
    while True:
        tmp += 6 * i
        if tmp >= N:
            total = i + 1
            break
        i += 1

print(total)
