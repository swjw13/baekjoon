# https://www.acmicpc.net/problem/16953
# A to B

from collections import deque
A, B = list(map(int, input().split()))
B_length = len(str(B))

queue = deque([(A, 0)])
answer = -2

while queue:
    cur_num, cur_turn = queue.popleft()
    if cur_num == B:
        answer = cur_turn
        break
    else:
        new_num = cur_num * 2
        if len(str(new_num)) <= B_length:
            queue.append((new_num, cur_turn + 1))
        new_num = str(cur_num) + "1"
        if len(new_num) <= B_length:
            queue.append((int(new_num), cur_turn + 1))

print(answer + 1)