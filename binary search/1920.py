# 원소 있는지 찾기

N = int(input())

lst = list(map(int, input().split()))

M = int(input())

finds = list(map(int, input().split()))

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


for i in finds:
    if binSearch(0, N - 1, i):
        print(1)
    else:
        print(0)
