import sys

N = int(sys.stdin.readline())
k = int(sys.stdin.readline())


def find_under(num):
    total = 0
    tmp = int(num ** 0.5)
    for i in range(1, tmp + 1):
        total += 2 * i - 1
    for i in range(tmp + 1, N + 1):
        total += num // i * 2
        if num % i == 0:
            total -= 2
    if tmp == num ** 0.5:
        total -= 1
    return total


start = 1
end = N * N
mx = 0

while True:
    if start > end:
        break
    mid = (start + end) // 2

    if find_under(mid) >= k:
        end = mid - 1
    else:
        start = mid + 1

print(end)
