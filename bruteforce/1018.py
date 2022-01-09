def compare_line(lst1, lst2):
    total = 0
    for i in range(8):
        if lst1[i] != lst2[i]:
            total += 1
    return total


N, M = list(map(int, input().split()))
palate = []
for _ in range(N):
    line = input()
    palate.append(line)

correct1 = 'BWBWBWBW'
correct2 = 'WBWBWBWB'

min_change = 10000

for i in range(N - 7):
    for j in range(M - 7):
        total1 = 0
        for k in range(8):
            if k % 2 == 0:
                total1 += compare_line(palate[i + k][j:j + 8], correct1)
            else:
                total1 += compare_line(palate[i + k][j:j + 8], correct2)
        total2 = 0
        for k in range(8):
            if k % 2 == 0:
                total2 += compare_line(palate[i + k][j:j + 8], correct2)
            else:
                total2 += compare_line(palate[i + k][j:j + 8], correct1)

        if min(total1, total2) < min_change:
            min_change = min(total1, total2)

print(min_change)
