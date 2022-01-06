A, B = input().split()
A, B = list(A), list(B)

first = None
on_count = 0
total = 0
i = 1

while True:
    if len(A) == 0:
        total += on_count * i
        first = "A"
        break
    elif len(B) == 0:
        total += on_count * i
        first = "B"
        break

    a = int(A.pop())
    b = int(B.pop())

    tmp = a + b
    total += (tmp % 10 + on_count) * i
    if tmp >= 10:
        on_count = 1
    else:
        on_count = 0
    i *= 10

if first == "B":
    while A:
        a = int(A.pop())
        total += a * i
        i *= 10
else:
    while B:
        b = int(B.pop())
        total += b * i
        i *= 10
print(total)
