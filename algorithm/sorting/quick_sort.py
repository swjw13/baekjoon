# https://www.acmicpc.net/problem/2750
# quick sort

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))


def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(lst, 0, len(lst) - 1)
for i in lst:
    print(i)
