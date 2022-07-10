# https://www.acmicpc.net/problem/1977
# 완전제곱수

N = int(input())
M = int(input())


def find(n):
    start = int(n ** 0.5)

    for i in range(max(start - 1, 1), start + 3):
        if n // i == i and n % i == 0:
            return i
    return -1


minimum = 0
cnt = 0
for i in range(N, M + 1):
    num = i ** 0.5
    if find(i) != -1:
        cnt += i
        if minimum == 0:
            minimum = i

if cnt == 0:
    print(-1)
else:
    print(cnt)
    print(minimum)
