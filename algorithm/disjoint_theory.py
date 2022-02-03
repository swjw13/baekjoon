import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

n, m = list(map(int, input().split()))
parent = [i for i in range(n + 1)]


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


for _ in range(m):
    work, point1, point2 = list(map(int, input().split()))
    if work == 0:
        union(point1, point2)
    else:
        a = find_parent(parent, point1)
        b = find_parent(parent, point2)

        if a == b:
            print("YES")
        else:
            print("NO")
