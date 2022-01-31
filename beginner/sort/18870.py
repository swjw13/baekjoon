import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

#중복제거
sorts = sorted(set(lst))


def bin_search(pivot, start, end):
    if start > end:
        return False
    mid = (start + end) // 2
    if sorts[mid] == pivot:
        return mid
    elif sorts[mid] < pivot:
        return bin_search(pivot, mid + 1, end)
    else:
        return bin_search(pivot, start, mid - 1)


n = len(sorts)
for i in lst:
    sys.stdout.write("%d " % (bin_search(i, 0, n)))
