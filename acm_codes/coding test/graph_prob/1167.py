import sys

input = sys.stdin.readline

V = int(input())
lines = [[] for _ in range(V + 1)]
leaves = []

for _ in range(V):
    lst = list(map(int, input().split()))
    length = len(lst)
    start_point = lst[0]

    for i in range(1, length - 1, 2):
        lines[start_point].append((lst[i], lst[i + 1]))

mx = 0
mx_node = None
visited_1 = [False for _ in range(V + 1)]
visited_2 = [False for _ in range(V + 1)]


def dfs(cur_point, length, visited):
    global mx
    global mx_node
    visited[cur_point] = True
    if length > mx:
        mx = length
        mx_node = cur_point
    for (connected_point, weight) in lines[cur_point]:
        if not visited[connected_point]:
            dfs(connected_point, length + weight, visited)


dfs(1, 0, visited_1)
dfs(mx_node, 0, visited_2)

print(mx)
