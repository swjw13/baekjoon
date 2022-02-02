import sys

n = int(sys.stdin.readline())
total = 0

for i in range(n):
    total += i + 1

sys.stdout.write("%d\n" % total)
