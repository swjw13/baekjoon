# https://www.acmicpc.net/problem/1991
# 트리 순회

import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
tree = defaultdict(list)

for _ in range(N):
    node, left, right = input().split()
    if left == "." and right == ".":
        tree[node] = []
    else:
        tree[node] = [left, right]


def preorder(cur_point):
    if len(tree[cur_point]) == 0:
        return cur_point
    elif tree[cur_point][0] == ".":
        return cur_point + preorder(tree[cur_point][1])
    elif tree[cur_point][1] == ".":
        return cur_point + preorder(tree[cur_point][0])
    else:
        return cur_point + preorder(tree[cur_point][0]) + preorder(tree[cur_point][1])


def inorder(cur_point):
    if len(tree[cur_point]) == 0:
        return cur_point
    elif tree[cur_point][0] == ".":
        return cur_point + inorder(tree[cur_point][1])
    elif tree[cur_point][1] == ".":
        return inorder(tree[cur_point][0]) + cur_point
    else:
        return inorder(tree[cur_point][0]) + cur_point + inorder(tree[cur_point][1])


def postorder(cur_point):
    if len(tree[cur_point]) == 0:
        return cur_point
    elif tree[cur_point][0] == ".":
        return postorder(tree[cur_point][1]) + cur_point
    elif tree[cur_point][1] == ".":
        return postorder(tree[cur_point][0]) + cur_point
    else:
        return postorder(tree[cur_point][0]) + postorder(tree[cur_point][1]) + cur_point

print(preorder("A"))
print(inorder("A"))
print(postorder("A"))