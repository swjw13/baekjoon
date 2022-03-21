# 카펫
# https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    answer = []
    total_capet = brown + yellow

    for i in range(1, int(total_capet ** 0.5) + 1):
        if total_capet % i != 0:
            continue
        w = i
        h = total_capet // w

        if brown == 2 * (w + h) - 4:
            answer = [h, w]

    return answer