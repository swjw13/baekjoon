import sys

while True:
    try:
        a, b = list(map(int, sys.stdin.readline().split()))
        sys.stdout.write("%d\n" % (a + b))

    except:
        break
