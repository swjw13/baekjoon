# 배수와 약수

while True:
    a, b = list(map(int, input().split()))
    if a==0 and  b==0:
        break
    if a % b == 0:
        print("multiple")
    elif b % a == 0:
        print("factor")
    else:
        print("neither")