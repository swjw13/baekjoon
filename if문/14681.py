import sys
x = int(sys.stdin.readline())
y = int(sys.stdin.readline())

if x * y > 0:
    if x < 0:
        print(3)
    else:
        print(1)
else:
    if x < 0 :
        print(2)
    else:
        print(4)