a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

for i in range(1, len(a)):
    j = i - 1
    while j >= 0 and a[j] > a[j + 1]:
        a[j], a[j + 1] = a[j + 1], a[j]
        j -= 1

print(a)
