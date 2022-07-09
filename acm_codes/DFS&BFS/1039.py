# https://www.acmicpc.net/problem/1039
# 교환

import sys
from collections import deque, defaultdict

input = sys.stdin.readline

N, K = list(map(int, input().split()))
length = len(list(str(N)))
idx = [1]
for _ in range(length):
    idx.append(idx[-1] * 10)


def find_each(num, n):
    start_idx = idx[n]
    end_idx = idx[n + 1]
    return (num % end_idx) // start_idx


queue = deque([(N, 0)])
ans = -1
visited = defaultdict(set)
while queue:
    cur_num, cur_turn = queue.popleft()
    if cur_turn == K:
        ans = max(ans, cur_num)
    else:
        for i in range(length):
            for j in range(i + 1, length):
                min_num = find_each(cur_num, i)
                max_num = find_each(cur_num, j)
                new_number = cur_num
                if min_num > max_num:
                    new_number -= (min_num - max_num) * idx[i]
                    new_number += (min_num - max_num) * idx[j]
                elif min_num < max_num:
                    new_number += (max_num - min_num) * idx[i]
                    new_number -= (max_num - min_num) * idx[j]
                if find_each(new_number, length - 1) != 0:
                    if new_number not in visited[cur_turn]:
                        visited[cur_turn].add(new_number)
                        queue.append((new_number, cur_turn + 1))

print(ans)
