T = int(input())


def find_i(num):
    i = 1
    while i * (i + 1) < num:
        i += 1
    return i


for _ in range(T):
    a, b = list(map(int, input().split()))
    i = find_i(b - a)

    if i * (i + 1) - (b - a) < i:
        print(2 * i)
    else:
        print(2 * i - 1)
