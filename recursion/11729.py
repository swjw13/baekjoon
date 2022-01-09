def hanoi_count(num):
    if num == 1:
        return 1
    return 2 * hanoi_count(num - 1) + 1


def hanoi(num, start, mid, end):
    if num == 1:
        print(start, end)
        return
    hanoi(num - 1, start, end, mid)
    hanoi(1, start, mid, end)
    hanoi(num - 1, mid, start, end)


n = int(input())
print(hanoi_count(n))
hanoi(n, 1, 2, 3)
