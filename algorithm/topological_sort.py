import sys
from collections import deque, defaultdict

input = sys.stdin.readline

N, M = list(map(int, input().split()))

# directed graph를 저장하기 위한 dict
line = defaultdict(set)

# 진입 차수를 저장하기 위한 dict
is_degree = defaultdict(int)

for _ in range(M):
    start, end = list(map(int, input().split()))
    line[start].add(end)
    is_degree[end] += 1

queue = []
for i in range(1, N + 1):
    if is_degree[i] == 0:
        queue.append(i)
queue = deque(queue)
ans = []

# 원리
# 진입차수가 0인 point들을 초기 queue로 잡고
# 하나씩 pop
# 연결된 노드들의 진입 차수를 1씩 줄이는데, 진입차수가 0이 된 점을 queue에 넣는다

while queue:
    student = queue.popleft()
    ans.append(student)

    for related_point in line[student]:
        is_degree[related_point] -= 1
        if is_degree[related_point] == 0:
            queue.append(related_point)

for i in ans:
    print(i, end=' ')
