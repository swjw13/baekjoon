# https://www.acmicpc.net/problem/2750
# radix sort

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
queue = deque()
index_1 = 1
index_2 = 10
hash_table = {i: deque() for i in range(10)}

for _ in range(N):
    queue.append(int(input()))

while True:
    while queue:
        value = queue.popleft()
        key = (value % index_2) // index_1
        hash_table[key].append(value)

    if len(hash_table[0]) == N:
        break

    for i in range(10):
        queue += hash_table[i]

    index_1 *= 10
    index_2 *= 10
    hash_table = {i: deque() for i in range(10)}

for i in queue:
    print(i)

