from collections import defaultdict
from collections import deque


def solution(info, edges):
    answer = 0
    lines = defaultdict(set)
    for start, end in edges:
        lines[start].add(end)

    stack = deque([(lines[0], 1, 0, {0})])
    while stack:
        connected, sheep_count, wolf_count, is_in = stack.popleft()
        answer = max(answer, sheep_count)

        for i in connected:
            if i not in is_in:
                if info[i] == 0:
                    stack.append((connected.union(lines[i]), sheep_count + 1, wolf_count, is_in.union({i})))
                else:
                    if sheep_count > wolf_count + 1:
                        stack.append((connected.union(lines[i]), sheep_count, wolf_count + 1, is_in.union({i})))

    return answer


a = [0,1,0,1,1,0,1,0,0,1,0]
b = 	[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
print(solution(a, b))
