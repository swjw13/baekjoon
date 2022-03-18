# 실패율
# https://programmers.co.kr/learn/courses/30/lessons/42889
# 2019 kakao

from bisect import bisect_left, bisect_right


def solution(N, stages):
    answer = [[i, 0.0] for i in range(N + 1)]

    stages.sort()
    length = len(stages)

    for i in range(1, N + 1):
        left_idx = bisect_left(stages, i)
        right_idx = bisect_right(stages, i)

        # stage에 도달한 사람
        one = length - left_idx

        # 클리어 하지 못한 사람 사람
        two = right_idx - left_idx

        if one == 0:
            answer[i][1] = 0
        else:
            answer[i][1] = two / one
    answer.sort(key=lambda x: (-x[1], x[0]))

    ans = []
    for i in range(N + 1):
        if answer[i][0] != 0:
            ans.append(answer[i][0])

    return ans

a = 4
b =[4,4,4,4,4]
print(solution(a, b))