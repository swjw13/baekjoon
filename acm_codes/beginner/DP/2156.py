N = int(input())
c = []
wine = []
for _ in range(N):
    step = int(input())
    wine.append(step)

c.append((0, 0))
c.append((wine[0], 1))

for i in range(2, N + 1):
    prev = c[i - 1][0]
    if c[i - 1][1] == 2:
        tmp = max(prev, c[i - 2][0] + wine[i - 1], c[i - 3][0] + wine[i - 2] + wine[i - 1])
        if tmp == prev:
            c.append((prev, 0))
        elif tmp == c[i - 2][0] + wine[i - 1]:
            c.append((c[i - 2][0] + wine[i - 1], 1))
        else:
            c.append((c[i - 3][0] + wine[i - 2] + wine[i - 1], 2))
    else:
        tmp = max(c[i - 1][0], c[i - 2][0])
        if tmp == c[i - 1][0]:
            c.append((c[i - 1][0] + wine[i - 1], 2))
        else:
            c.append((c[i - 2][0] + wine[i - 1], 1))

print(c[-1][0])
