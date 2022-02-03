import sys

T = sys.stdin.readline()
T = int(T)

for i in range(T):
    a, b = list(map(int, sys.stdin.readline().split()))
    print("Case #{}: {}".format(i+1, a+b))