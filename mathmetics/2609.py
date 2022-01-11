# 최대공약수와 최소공배수

def lcs(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1
    while num1 % num2 != 0:
        num1, num2 = num2, num1 % num2
    return num2


a, b = list(map(int, input().split()))
lower = lcs(a, b)
print(lower)
print(a * b // lower)