# 표 편집
# https://programmers.co.kr/learn/courses/30/lessons/81303
# 2021 kakao
# 부분 해결

from collections import deque

def solution(n, k, cmd):
    answer = ''

    cur_idx = k
    was_remain = [[i - 1, i + 1] for i in range(n)]
    is_remain = [True for _ in range(n)]
    total_length = len(was_remain)
    deleted = deque()

    def up(idx, count):
        for _ in range(count):
            idx -= 1
            while idx >= 0 and not is_remain[idx]:
                idx -= 1
            if idx < 0:
                return idx
        return idx

    def down(idx, count, length):
        for _ in range(count):
            idx += 1
            while idx < length and not is_remain[idx]:
                idx += 1
            if idx == length:
                return idx
        return idx

    for i in cmd:
        options = i.split()
        if options[0] == "U":
            cur_idx = up(cur_idx, int(options[1]))
        elif options[0] == "D":
            cur_idx = down(cur_idx, int(options[1]), n)
        elif options[0] == "Z":
            idx_to_recover = deleted.pop()
            is_remain[idx_to_recover] = True

        elif options[0] == "C":
            is_remain[cur_idx] = False
            deleted.append(cur_idx)
            tmp = cur_idx
            cur_idx = down(cur_idx, 1, total_length)
            if cur_idx == total_length:
                cur_idx = tmp
                cur_idx = up(cur_idx, 1)

    for i in is_remain:
        if i:
            answer += "O"
        else:
            answer += "X"
    return answer
