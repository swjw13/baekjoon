import sys

N = int(input())
lst = []

for _ in range(N):
    x, y = list(map(int, sys.stdin.readline().split()))
    lst.append((x, y))

lst.sort(key=lambda x: (x[0], x[1]))
for i in lst:
    sys.stdout.write("%d %d\n" % (i[0], i[1]))
