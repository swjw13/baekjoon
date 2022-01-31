from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, K = list(map(int, input().split()))

final = 2 * max(N, K) + 1
mp = [0 for _ in range(final)]
mp[N] = 1
queue = deque([(N, 0)])
while queue:
    point, turn = queue.popleft()
    if point == K:
        print(turn)
        break
    one = point - 1
    two = point + 1
    three = 2 * point

    if one >= 0 and mp[one] == 0:
        queue.append((one, turn + 1))
        mp[one] = 1
    if two < final and mp[two] == 0:
        queue.append((two, turn + 1))
        mp[two] = 1
    if three < final and mp[three] == 0:
        queue.append((three, turn + 1))
        mp[three] = 1
