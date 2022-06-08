import sys

year = int(sys.stdin.readline())
yun = 0

if year % 400 == 0:
    yun = 1
elif year % 100 == 0:
    yun = 0
elif year % 4 == 0:
    yun = 1

print(yun)