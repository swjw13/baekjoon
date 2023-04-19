from collections import defaultdict

group_num = 0


def get_new_group():
    global group_num
    group_num += 1
    return group_num


def solution(commands):
    answer = []
    group_value = defaultdict(str)

    cell = [[0 for _ in range(51)] for _ in range(51)]
    for row in range(1, 51):
        for col in range(1, 51):
            cell[row][col] = get_new_group()

    for c in commands:
        command = c.split()
        if command[0] == "UPDATE":
            if len(command) == 4:
                row_to_find = int(command[1])
                col_to_find = int(command[2])
                value_to_insert = command[3]

                g_num = cell[row_to_find][col_to_find]
                group_value[g_num] = value_to_insert

            elif len(command) == 3:
                value1 = command[1]
                value2 = command[2]
                for key in group_value.keys():
                    if group_value[key] == value1:
                        group_value[key] = value2

        elif command[0] == "MERGE":
            r1 = int(command[1])
            c1 = int(command[2])
            r2 = int(command[3])
            c2 = int(command[4])

            group1 = cell[r1][c1]
            group2 = cell[r2][c2]
            if group1 == group2:
                continue

            value1 = group_value[group1]
            value2 = group_value[group2]

            if len(value1) == 0:
                for row in range(1, 51):
                    for col in range(1, 51):
                        if cell[row][col] == group1:
                            cell[row][col] = group2
                if len(value1) != 0:
                    group_value.pop(group1)
            else:
                for row in range(1, 51):
                    for col in range(1, 51):
                        if cell[row][col] == group2:
                            cell[row][col] = group1
                if len(value2) != 0:
                    group_value.pop(group2)

        elif command[0] == "UNMERGE":
            row_to_find = int(command[1])
            col_to_find = int(command[2])
            group_to_unmerge = cell[row_to_find][col_to_find]
            remain_value = group_value[group_to_unmerge]

            for row in range(1, 51):
                for col in range(1, 51):
                    if cell[row][col] == group_to_unmerge:
                        cell[row][col] = get_new_group()

            group_value.pop(group_to_unmerge)

            if len(remain_value) != 0:
                new_group = cell[row_to_find][col_to_find]
                group_value[new_group] = remain_value

        elif command[0] == "PRINT":
            row_to_find = int(command[1])
            col_to_find = int(command[2])
            g_num = cell[row_to_find][col_to_find]
            g_value = group_value[g_num]
            if len(g_value) == 0:
                answer.append("EMPTY")
            else:
                answer.append(g_value)

    return answer
