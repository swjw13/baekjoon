n = int(input())
lst = [[0, 0] for i in range(n + 1)]
lst[1] = [1, 0]
lst[2] = [2, 0]
lst[3] = [3, 0]

for i in range(4, n + 1):
    one_before = lst[i - 1]
    tmp = [one_before[0] + 1, one_before[1]]

    three_before = lst[i - 3]

    if one_before[1] != 0 and sum(one_before) >= tmp[0]:
        tmp = [sum(one_before), one_before[1]]

    if 2 * three_before[0] >= tmp[0]:
        tmp = [2 * three_before[0], three_before[0]]

    lst[i] = tmp

# print(lst[n][0])
print(lst)