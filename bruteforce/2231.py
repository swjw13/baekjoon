def divsum(num):
    total = 0
    i = 1
    while True:
        tmp = num // i
        if tmp == 0:
            break
        total += tmp % 10
        i *= 10
    return num + total


N = int(input())
for i in range(N):
    if divsum(i) == N:
        print(i)
        break
if i == N-1:
    print(0)
