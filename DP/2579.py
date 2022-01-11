N = int(input())
c = []
stair = []
for _ in range(N):
    step = int(input())
    stair.append(step)

c.append((0, 0))
c.append((stair[0], 1))

for i in range(2, N + 1):
    if c[i - 1][1] == 2:
        tmp = max(c[i-2][0], c[i-3][0] + stair[i-2])
        if tmp == c[i - 2][0]:
            c.append((c[i - 2][0] + stair[i - 1], 1))
        else:
            c.append((c[i-3][0] + stair[i-2]+stair[i-1],2))
    else:
        tmp = max(c[i - 1][0], c[i - 2][0])
        if tmp == c[i - 1][0]:
            c.append((tmp + stair[i - 1], c[i - 1][1] + 1))
        else:
            c.append((tmp + stair[i - 1], 1))

print(c[-1][0])
