import sys

input = sys.stdin.readline

N = int(input())

none_batch = 1
one_batch = 1
total = 3

for i in range(1, N):
    none = total
    one = none_batch + one_batch

    total = none + 2 * one
    none_batch = none
    one_batch = one

print(total % 9901)
