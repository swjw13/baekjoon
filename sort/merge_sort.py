# 10814
import sys


def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0][0] <= right[0][0]:
                result.append(left[0])
                left.pop(0)
            else:
                result.append(right[0])
                right.pop(0)
        elif len(left) > 0:
            result += left
            left = []
        elif len(right) > 0:
            result += right
            right = []
    return result


def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    leftList = lst[:mid]
    rightList = lst[mid:]
    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)
    return merge(leftList, rightList)


N = int(sys.stdin.readline())
membership = []
for _ in range(N):
    age, name = sys.stdin.readline().split()
    membership.append((int(age), name))
answer = merge_sort(membership)

for i in answer:
    sys.stdout.write("%d %s\n" % (i[0], i[1]))
