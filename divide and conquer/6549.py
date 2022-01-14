import sys


def square(low, high, lst):
    if low == high:
        return lst[low]
    mid = (low + high) // 2

    side = max(square(low, mid, lst), square(mid + 1, high, lst))

    mid_tall = min(lst[mid], lst[mid + 1])
    side = max(side, mid_tall * 2)

    lo = mid
    hi = mid + 1
    while lo > low and hi < high:
        if lst[lo - 1] > lst[hi + 1]:
            lo -= 1
            if mid_tall > lst[lo]:
                mid_tall = lst[lo]
        else:
            hi += 1
            if lst[hi] < mid_tall:
                mid_tall = lst[hi]

        side = max(side, mid_tall * (hi - lo + 1))
    if lo == low:
        while hi < high:
            hi += 1
            if lst[hi] < mid_tall:
                mid_tall = lst[hi]
            side = max(side, mid_tall * (hi - lo + 1))
    else:
        while lo > low:
            lo -= 1
            if mid_tall > lst[lo]:
                mid_tall = lst[lo]
            side = max(side, mid_tall * (hi - lo + 1))

    return side


while True:
    lst = list(map(int, sys.stdin.readline().split()))
    if len(lst) == 1:
        break

    # lst: 높이를 저장하는 배열
    n = lst.pop(0)
    print(square(0, n - 1, lst))
