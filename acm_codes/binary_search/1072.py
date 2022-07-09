# https://www.acmicpc.net/problem/1072
# 게임
import sys
input = sys.stdin.readline

X, Y = list(map(int, input().split()))
ans = Y * 100 // X
if X == Y:
    print(-1)
else:
    idx = -1
    start = 0
    end = 1000000000
    while start <= end:
        mid = (start + end) // 2
        if ((Y + mid) * 100 // (X + mid)) - ans >= 1:
            idx = mid
            end = mid - 1
        else:
            start = mid + 1

    print(idx)