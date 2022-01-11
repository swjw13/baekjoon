# 나눴을 때 나머지가 같은 수 구하기

def LCS(num1, num2):
    a = num1
    b = num2
    if a < b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b
    return b


N = int(input())
numbers = []
after = set()
for _ in range(N):
    m = int(input())
    for prev in numbers:
        after.add(abs(m - prev))
    numbers.append(m)

after = list(after)
k = after.pop(0)
while len(after) != 0:
    tmp = after.pop(0)
    k = LCS(k, tmp)

a = set()
a.add(k)
for i in range(2, int(k ** 0.5) + 1):
    if k % i == 0:
        a.add(i)
        a.add(k // i)
a = list(a)
a.sort()
for i in a:
    print(i, end=' ')
