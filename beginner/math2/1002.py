import sys

t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = list(map(int, sys.stdin.readline().split()))

    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    elif ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 > r1 + r2:
        print(0)
    elif ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 == r1 + r2:
        print(1)
    elif ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 == abs(r1 - r2):
        print(1)
    elif ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 < abs(r1 - r2):
        print(0)
    else:
        print(2)
