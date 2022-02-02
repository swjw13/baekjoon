# 링 돌아가는 비율

def lcs(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1
    while num1 % num2 != 0:
        num1, num2 = num2, num1 % num2
    return num2


N = int(input())
lst = list(map(int, input().split()))

pivot = lst.pop(0)
for i in lst:
    lower = lcs(pivot, i)
    print("{}/{}".format(pivot // lower, i // lower))