T = int(input())

map = [[0 for _ in range(15)] for _ in range(15)]

for i in range(1,15):
    for j in range(0,15):
        if i == 1:
            map[i][j] = 1
        elif j == 0:
            map[i][j] = i
        else:
            map[i][j] = map[i-1][j] + map[i][j-1]

for _ in range(T):
    k = int(input())
    n = int(input())
    print(map[n][k])
