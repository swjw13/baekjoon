# https://www.acmicpc.net/problem/1062
# 가르침

import sys
from itertools import combinations
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

N, K = list(map(int, input().split()))
words = []
idx = [1]
for i in range(25):
    idx.append(idx[-1] * 2)
s = "abcdefghijklmnopqrstuvwxyz"
num_dict = dict()
for i in range(26):
    num_dict[s[i]] = idx[i]

for _ in range(N):
    w = set(list(input().strip()))
    bit = 0
    for i in w:
        bit += num_dict[i]
    words.append(bit)

must_num = 0
must = []

for w in "antic":
    must_num += num_dict[w]
    must.append(num_dict[w])

for i in must:
    idx.remove(i)

if K < 5:
    print(0)
elif K == 5:
    cnt = 0
    for each_word in words:
        if each_word == sum(must):
            cnt += 1
    print(cnt)
else:
    ans = -1
    for i in combinations(idx, K - 5):
        total = must_num + sum(i)
        cnt = 0
        for each_word in words:
            if each_word & total == each_word:
                cnt += 1

        ans = max(ans, cnt)
    print(ans)