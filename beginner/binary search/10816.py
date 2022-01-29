# 원소의 갯수

N = int(input())
lst = list(map(int, input().split()))
M = int(input())
find = list(map(int, input().split()))

lst.sort()

def binSearch(start, end, value):
    if start > end:
        return False
    mid = (start + end) // 2
    if lst[mid] == value:
        return True
    elif lst[mid] > value:
        return binSearch(start, mid - 1, value)
    else:
        return binSearch(mid + 1, end, value)


from bisect import bisect_left, bisect_right

for i in find:
    left = bisect_left(lst, i)
    right = bisect_right(lst, i)
    print(right - left, end=" ")