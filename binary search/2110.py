import sys

N, C = list(map(int, sys.stdin.readline().split()))
lst = []
for _ in range(N):
    lst.append(int(sys.stdin.readline()))
lst.sort()

start = 1
end = lst[-1] - lst[0]
mx = 0
if N == 2:
    print(lst[1] - lst[0])
else:
    while True:
        if start >= end:
            break
        mid = (start + end) // 2
        count = 1
        tmp = lst[0]
        for i in range(1, N):
            if lst[i] - tmp >= mid:
                count += 1
                tmp = lst[i]

        if count >= C:
            mx = mid
            start = mid + 1
        else:
            end = mid

    print(mx)
