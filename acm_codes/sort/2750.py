import sys
sys.setrecursionlimit(10**6)
N = int(input())
lst = []
for _ in range(N):
    n = int(input())
    lst.append(n)


def sort(nums):
    if len(nums) == 0:
        return []
    pivot = nums[0]
    first = [ir for ir in nums if ir < pivot]
    middle = [iq for iq in nums if iq == pivot]
    last = [ip for ip in nums if ip > pivot]
    return sort(first) + middle + sort(last)


for i in sort(lst):
    print(i)
