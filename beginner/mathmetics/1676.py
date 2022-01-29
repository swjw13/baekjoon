# 팩토리얼 0의 갯수

def counting(num, how=2):
    two = 0
    while num % how == 0:
        two += 1
        num //= how
    return two


N = int(input())
two = 0
five = 0

for i in range(1, N + 1):
    two += counting(i, 2)
    five += counting(i, 5)

print(min(two, five))
