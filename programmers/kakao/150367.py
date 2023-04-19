from collections import defaultdict


def find_binary_tree(num):
    res = ""
    while num > 0:
        res = str(num % 2) + res
        num //= 2

    full_length = 1
    while full_length <= len(res):
        full_length *= 2
    full_length -= 1
    while len(res) < full_length:
        res = "0" + res

    return res


order_cache = defaultdict(str)


def searching(cur_idx, length):
    if 2 * cur_idx > length and 2 * cur_idx + 1 > length:
        return str(cur_idx) + " "
    else:
        left = searching(2 * cur_idx, length)
        right = searching(2 * cur_idx + 1, length)
        return left + str(cur_idx) + " " + right


def inorder(length):
    if len(order_cache[length]) != 0:
        return order_cache[length]
    else:
        res = searching(1, length)
        order_cache[length] = res
        return res


def solution(numbers):
    answer = []

    for number in numbers:
        unavailable = False
        num_binary = find_binary_tree(number)

        length = len(num_binary)
        orders = inorder(length)
        order_split = orders.split()

        tree = [0 for _ in range(length + 1)]
        for i in range(length):
            idx = int(order_split[i])
            tree[idx] = int(num_binary[i])

        for i in range(2, length + 1):
            if tree[i] != 0:
                if tree[i // 2] == 0:
                    unavailable = True
                    break

        if unavailable:
            answer.append(0)
        else:
            answer.append(1)

    return answer


a = [i for i in range(1, 100)]
print(solution(a))