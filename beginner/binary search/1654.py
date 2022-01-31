# 랜선 자르기

import sys

N, K = list(map(int, input().split()))
lines = []
for _ in range(N):
    lines.append(int(sys.stdin.readline()))

start = 0
end = 2**31 - 1
max = 0

while True:
    if end < start:
        break
    total = 0
    mid = (start + end) // 2
    for i in lines:
        total += i // mid
    if total >= K:
        max = mid
        start = mid + 1
    else:
        end = mid - 1

print(max)
