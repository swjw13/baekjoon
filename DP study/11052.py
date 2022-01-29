N = int(input())
cards = list(map(int, input().split()))

cards.insert(0, 0)
mx = [0]

for i in range(1, N + 1):
    tmp = cards[i]

    for k in range(1, len(mx) // 2 + 1):
        tmp = max(tmp, mx[k] + mx[len(mx) - k])

    mx.append(tmp)
print(mx[-1])