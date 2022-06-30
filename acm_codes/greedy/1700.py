# https://www.acmicpc.net/problem/1700
# 멀티탭 스케쥴링

import sys
from bisect import bisect_left
from collections import defaultdict
input = sys.stdin.readline

N, K = list(map(int, input().split()))
lst = list(map(int, input().split()))

if N >= len(set(lst)):
    print(0)
else:
    ans = 0
    where = defaultdict(list)
    count = defaultdict(int)
    for i in range(K):
        where[lst[i]].append(i)

    idx = 0
    plug = set()
    while len(plug) != N:
        plug.add(lst[idx])
        idx += 1

    print(plug)
    print(where)

    while idx < K:
        if lst[idx] in plug:
            idx += 1
        else:
            least_plug = -1
            least_num = 0
            for i in plug:
                tmp = bisect_left(where[i], idx)

                if tmp == len(where[i]):
                    a = K
                else:
                    a = where[i][tmp]

                if least_num < a:
                    least_plug = i
                    least_num = a
            plug.remove(least_plug)
            plug.add(lst[idx])
            ans += 1
            idx += 1
    print(ans)