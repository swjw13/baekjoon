import sys

T = int(sys.stdin.readline())

for i in range(T):
    a, b = list(map(int, sys.stdin.readline().split()))
    sys.stdout.write("%d\n"%(a+b))