# https://programmers.co.kr/learn/courses/30/lessons/12946
# 하노이의 탑

def solution(n):
    answer = []

    def hanoi(res, fr, mid, to):
        if res == 1:
            answer.append([fr + 1, to + 1])
        else:
            hanoi(res - 1, fr, to, mid)
            hanoi(1, fr, mid, to)
            hanoi(res - 1, mid, fr, to)

    hanoi(n, 0, 1, 2)

    return answer

a = 2
print(solution(a))
