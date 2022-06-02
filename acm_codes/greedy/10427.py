# https://www.acmicpc.net/problem/10427
# 빚

import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    lst = list(map(int, input().split()))
    N = lst[0]
    numbers = lst[1:]

    numbers.sort()

    part_total = [numbers[0]]
    for i in range(len(numbers) - 1):
        tmp = part_total[-1] + numbers[i + 1]
        part_total.append(tmp)

    ans = dict()
    memory = set()
    ans[1] = 0

    for i in range(1, len(numbers)):
        second = part_total[i]
        n = numbers[i]
        for j in range(i - 1, -1, -1):
            tmp = second - part_total[j] + numbers[j]
            count = i - j + 1
            if count not in memory:
                ans[count] = count * n - tmp
                memory.add(count)
            else:
                ans[count] = min(ans[count], count * n - tmp)

    total = 0
    for i in range(1, N + 1):
        total += ans[i]
        
    sys.stdout.write("{}\n".format(total))
