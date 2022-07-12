# https://www.acmicpc.net/problem/1735
# 분수 합

def gcd(a, b):
    if b > a:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b
    return b

a1, b1 = list(map(int, input().split()))
a2, b2 = list(map(int, input().split()))

up = a2 * b1 + a1 * b2
down = b1 * b2

g = gcd(up, down)

print(up // g, down // g)