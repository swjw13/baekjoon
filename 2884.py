import sys

H, M = list(map(int, sys.stdin.readline().split()))

if M - 45 >= 0:
   print("{} {}".format(H, M-45))
else:
    if H == 0:
        print("{} {}".format(23, M+15))
    else:
        print("{} {}".format(H-1, M+15))