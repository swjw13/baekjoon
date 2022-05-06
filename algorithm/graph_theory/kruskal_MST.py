import sys
import heapq

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

v, e = list(map(int, input().split()))

parent = [i for i in range(v + 1)]


def find_parent(lst, point):
    if lst[point] != point:
        lst[point] = find_parent(lst, lst[point])
    return lst[point]


def union(one, two):
    one = find_parent(parent, one)
    two = find_parent(parent, two)

    final_parent = min(one, two)
    parent[one] = final_parent
    parent[two] = final_parent

# 초기: [1, 2, 3, 4, 5, 6, 7, 8]
# 결과: [1, 1, 1, 1, 5, 5, 5, 8]


lines = []
for _ in range(e):
    lines.append(list(map(int, input().split())))

lines.sort(key=lambda x: x[2])

points_appended = set()
weight = 0

while lines:
    point1, point2, value = heapq.heappop(lines)

    a = find_parent(parent, point1)
    b = find_parent(parent, point2)

    if a != b:
        weight += value
        union(point1, point2)
        points_appended.add(point1)
        points_appended.add(point2)

print(weight)