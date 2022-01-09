import sys

sys.setrecursionlimit(10 ** 6)

print("quick sort")
a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


def quick_sort(nums):
    if len(nums) == 0:
        return []
    pivot = nums[0]
    first = [ir for ir in nums if ir < pivot]
    middle = [iq for iq in nums if iq == pivot]
    last = [ip for ip in nums if ip > pivot]
    return quick_sort(first) + middle + quick_sort(last)


print(quick_sort(a))
