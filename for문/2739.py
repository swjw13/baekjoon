import sys

n = int(sys.stdin.readline())

for i in range(8):
    print("2 * {} = {} ".format(i + 1, n * (i + 1)))
print("2 * {} = {}".format(9, n * 9))