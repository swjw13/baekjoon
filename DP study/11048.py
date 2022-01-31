N, M = list(map(int, input().split()))
house = []
for _ in range(N):
    house.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        tmp = house[i][j]
        if 0 <= i - 1:
            tmp = max(tmp, house[i - 1][j] + house[i][j])
        if 0 <= j - 1:
            tmp = max(tmp, house[i][j - 1] + house[i][j])
        if 1 <= i and 1 <= j:
            tmp = max(tmp, house[i - 1][j - 1] + house[i][j])

        house[i][j] = tmp

print(house[N - 1][M - 1])
