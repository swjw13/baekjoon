import sys

while True:
    a, b = list(map(int, sys.stdin.readline().split()))
    if a == 0 and b == 0:
        break
    sys.stdout.write("%d\n" % (a + b))
