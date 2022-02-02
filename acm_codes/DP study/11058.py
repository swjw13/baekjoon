n = int(input())
lst = [[0, 1] for i in range(n + 1)]
lst[1] = [1, 1]

for i in range(2, n + 1):
    one_before = lst[i - 1]
    three_before = lst[i - 3]
    four_before = lst[i - 4]

    default = [one_before[0] + one_before[1], one_before[1]]
    if i - 3 >= 0 and three_before[0] + 3 * three_before[1] >= default[0]:
        default = [three_before[0] + 3 * three_before[1], three_before[1]]
    if i - 3 >= 0 and 2 * three_before[0] >= default[0]:
        default = [2 * three_before[0], three_before[0]]
    if i - 4 >= 0 and 3 * four_before[0] >= default[0]:
        default = [3 * four_before[0], four_before[0]]
    lst[i] = default

print(lst[n][0])
