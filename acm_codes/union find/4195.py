# https://www.acmicpc.net/problem/4195
# 친구 네트워크

from collections import defaultdict
import sys

T = int(input())


def find_parent(lst, point):
    if lst[point] != point:
        lst[point] = find_parent(lst, lst[point])
    return lst[point]


for _ in range(T):
    N = int(input())

    name_to_num = dict()
    network_count = defaultdict(int)
    already_in_graph = set()
    parent = dict()

    tmp = 1
    for _ in range(N):
        one, two = input().split()
        if one not in already_in_graph:
            name_to_num[one] = tmp
            parent[tmp] = tmp
            tmp += 1
        if two not in already_in_graph:
            name_to_num[two] = tmp
            parent[tmp] = tmp
            tmp += 1

        one_number = name_to_num[one]
        two_number = name_to_num[two]

        if (one not in already_in_graph) and (two not in already_in_graph):
            already_in_graph.add(one)
            already_in_graph.add(two)

            if one_number > two_number:
                parent[one_number] = two_number
                network_count[two_number] = 2

            else:
                parent[two_number] = one_number
                network_count[one_number] = 2

        elif one not in already_in_graph:
            group = find_parent(parent, two_number)
            already_in_graph.add(one)
            parent[one_number] = group
            network_count[group] += 1

        elif two not in already_in_graph:
            group = find_parent(parent, one_number)
            already_in_graph.add(two)
            parent[two_number] = group
            network_count[group] += 1

        else:
            g1 = find_parent(parent, one_number)
            g2 = find_parent(parent, two_number)
            if g1 < g2:
                network_count[g1] += network_count[g2]
                parent[g2] = g1
                network_count[g2] = 0
            elif g1 > g2:
                network_count[g2] += network_count[g1]
                parent[g1] = g2
                network_count[g1] = 0

        fin = find_parent(parent, one_number)
        print(network_count[fin])
