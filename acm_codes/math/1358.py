# https://www.acmicpc.net/problem/1358
# 하키

import sys
input = sys.stdin.readline

W, H, X, Y, P = list(map(int, input().split()))

def rectangle(x, y):
    if X <= x <= X + W and Y <= y <= Y + H:
        return True
    else:
        return False
def circle(x, y):
    r = H / 2
    if x <= X:
        if (x - X) * (x - X) + (y - (Y + r)) * (y - Y - r) <= r * r:
            return True
        else:
            return False
    elif x >= X + W:
        if (x - (X + W)) * (x - (X + W)) + (y - (Y + r)) * (y - (Y + r)) <= r * r:
            return True
        else:
            return False
    else:
        return False

cnt = 0
for _ in range(P):
    x, y = list(map(int, input().split()))
    if rectangle(x, y) or circle(x, y):
        cnt += 1
print(cnt)