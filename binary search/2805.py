# 나무 절단

N, M = list(map(int, input().split()))

lst = list(map(int, input().split()))

start = 0
end = 1000000000
max = 0

while True:
    if start > end:
        break

    mid = (start + end) // 2

    total = 0
    for i in lst:
        if i >= mid:
            total += i - mid
        if total > M:
            break

    if total >= M:
        start = mid + 1
        max = mid
    else:
        end = mid - 1

print(max)
