from collections import deque


def solution(a):
    answer = 0

    def star(lst, n):
        tmp = {a[lst[0]], a[lst[1]]}
        for i in range(2, n, 2):
            tmp = tmp.intersection({a[lst[i]], a[lst[i + 1]]})
            if len(tmp) == 0:
                return False
        return True

    stack = deque()
    stack.append(([0], 1))
    stack.append(([], 1))

    while stack:
        prev, cur_point = stack.pop()
        if cur_point == len(a):
            continue
        new_prev = prev + [cur_point]
        new_length = len(new_prev)
        if new_length % 2 == 0:
            if star(new_prev, new_length):
                answer = max(answer, new_length)
                if cur_point < len(a) - 1:
                    stack.append((new_prev, cur_point + 1))
        else:
            if cur_point < len(a) - 1:
                stack.append((new_prev, cur_point + 1))
        if cur_point < len(a) - 1:
            stack.append((prev, cur_point + 1))

    return answer


a = [5,2,3,3,5,3]
print(solution(a))
