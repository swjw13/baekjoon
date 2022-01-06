T = int(input())

for _ in range(T):
    lst = list(map(int, input().split()))

    total = 0
    for i in lst[1:]:
        total += i
    avg = total / lst[0]

    sc = len([i for i in lst[1:] if i > avg])
    print("%.3f%%" % (sc / lst[0] * 100))
