lst = [[[1 for _ in range(25)] for _ in range(25)] for _ in range(25)]

for i in range(1, 21):
    for j in range(1, 21):
        for k in range(1, 21):
            if i < j < k:
                lst[i][j][k] = lst[i][j][k - 1] + lst[i][j - 1][k - 1] - lst[i][j - 1][k]
            else:
                lst[i][j][k] = lst[i - 1][j][k] + lst[i - 1][j - 1][k] + lst[i - 1][j][k - 1] - lst[i - 1][j - 1][k - 1]

while True:
    a, b, c = list(map(int, input().split()))

    y = 0
    if a == -1 and b == -1 and c == -1:
        break
    if a <= 0 or b <= 0 or c <= 0:
        y = 1
    elif a > 20 or b > 20 or c > 20:
        y = lst[20][20][20]
    else:
        y = lst[a][b][c]
    print("w({}, {}, {}) = {}".format(a, b, c, y))
