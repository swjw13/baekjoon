import sys

max_idx = None
max = 0
for i in range(9):
    num = int(sys.stdin.readline())
    if num > max:
        max = num
        max_idx = i+1

print(max)
print(max_idx)