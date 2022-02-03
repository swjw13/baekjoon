N, M = list(map(int, input().split()))
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

M, K = list(map(int, input().split()))
B_row = [[] for _ in range(K)]

for _ in range(M):
    lst = list(map(int, input().split()))
    for i in range(K):
        B_row[i].append(lst[i])

for i in range(N):
    for j in range(K):
        total = 0
        for p in range(M):
            total += A[i][p] * B_row[j][p]
        print(total, end=" ")
    print()
