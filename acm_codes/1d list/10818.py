import sys
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

sys.stdout.write("%d %d\n"%(min(lst), max(lst)))
