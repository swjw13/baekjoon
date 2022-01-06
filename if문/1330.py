import sys

a, b = list(map(int, sys.stdin.readline().split()))
st = None
if a < b:
    st = "<"
elif a > b:
    st = ">"
else:
    st = "=="

print(st)