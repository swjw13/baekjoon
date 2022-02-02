from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    check_bipartite = False

    V, E = list(map(int, input().split()))

    lines = [[] for _ in range(V + 1)]
    group = [0 for _ in range(V + 1)]
    visited = [False for _ in range(V + 1)]

    for _ in range(E):
        start, end = list(map(int, input().split()))
        lines[start].append(end)
        lines[end].append(start)

    for i in range(1, V + 1):
        if not visited[i]:
            queue = deque([i])
            group[i] = -1
            visited[i] = True

            while queue:
                current_point = queue.popleft()
                current_group = group[current_point]

                lst = lines[current_point]

                for points in lst:
                    if not visited[points]:
                        group[points] = current_group * -1
                        visited[points] = True
                        queue.append(points)

                    elif visited[points] and group[points] == current_group:
                        check_bipartite = True

                if check_bipartite:
                    break
        if check_bipartite:
            break

    if check_bipartite:
        print("NO")
    else:
        print("YES")
