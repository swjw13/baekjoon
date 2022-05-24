import sys

costs = [0, 0, 0]
tmp = [0,0,0]
N = int(sys.stdin.readline())
for _ in range(N):
    cost = list(map(int, sys.stdin.readline().split()))

    tmp[0] = min(costs[1], costs[2]) + cost[0]
    tmp[1] = min(costs[0], costs[2]) + cost[1]
    tmp[2] = min(costs[0], costs[1]) + cost[2]

    costs = tmp.copy()

print(min(costs))