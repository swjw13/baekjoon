# 최소공배수

def lcs(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1
    while num1 % num2 != 0:
        num1, num2 = num2, num1 % num2
    return num2


T = int(input())

for _ in range(T):
    a, b = list(map(int, input().split()))
    print(a * b // lcs(a, b))