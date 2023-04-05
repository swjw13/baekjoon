import sys

input = sys.stdin.readline
dxdy = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

n, m, k = list(map(int, input().split()))
add_list = []
for _ in range(n):
    lst = list(map(int, input().split()))
    add_list.append(lst)

board = [[5 for _ in range(n)] for _ in range(n)]
trees = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, z = list(map(int, input().split()))
    trees[x - 1][y - 1].append(z)

for _ in range(k):
    new_tree = [[[] for _ in range(n)] for _ in range(n)]
    summer_trees = []
    fall_trees = []
    for row in range(n):
        for col in range(n):
            if len(trees[row][col]) != 0:
                trees[row][col].sort()
                for sub_tree in trees[row][col]:
                    if board[row][col] >= sub_tree:
                        board[row][col] -= sub_tree
                        new_tree[row][col].append(sub_tree + 1)
                        if (sub_tree + 1) % 5 == 0:
                            for (dx, dy) in dxdy:
                                new_row = row + dx
                                new_col = col + dy
                                if 0 <= new_row < n and 0 <= new_col < n:
                                    new_tree[row + dx][col + dy].append(1)
                    else:
                        summer_trees.append((row, col, sub_tree))

    for (row, col, nut) in summer_trees:
        board[row][col] += nut // 2

    for row in range(n):
        for col in range(n):
            board[row][col] += add_list[row][col]
            trees[row][col] = new_tree[row][col]
            trees[row][col].sort()

cnt = 0
for row in range(n):
    for col in range(n):
        cnt += len(trees[row][col])
print(cnt)
