# 배낭 문제

N, K = list(map(int, input().split()))
things = []
for _ in range(N):
    W, V = list(map(int, input().split()))
    things.append((W, V))

values = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        w = things[i - 1][0]
        v = things[i - 1][1]

        if j < w:
            values[i][j] = values[i - 1][j]
        else:
            values[i][j] = max(v + values[i - 1][j - w], values[i - 1][j])

print(values[N][K])
