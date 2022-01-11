# 조합 0 의 갯수

def counting(num, how=2):
    count = 0
    while num % how == 0:
        count += 1
        num //= how
    return count


n, m = list(map(int, input().split()))

up_2 = 0
up_5 = 0
down_2 = 0
down_5 = 0

a = 2
while a <= n:
    up_2 += n // a
    a *= 2
b = 5
while b <= n:
    up_5 += n // b
    b *= 5

c = 2
while c <= m:
    down_2 += m // c
    c *= 2
d = 2
while d <= n - m:
    down_2 += (n - m) // d
    d *= 2
e = 5
while e <= m:
    down_5 += m // e
    e *= 5
f = 5
while f <= n - m:
    down_5 += (n - m) // f
    f *= 5

print(min(up_2 - down_2, up_5 - down_5))
