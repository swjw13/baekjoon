# 멀쩡한 사각형
# https://programmers.co.kr/learn/courses/30/lessons/62048

def solution(w, h):
    answer = w * h

    def gcd(a, b):
        if a < b:
            b, a = a, b
        while True:
            if a % b == 0:
                break
            else:
                a, b = b, a % b
        return b
    if w == 1 or h == 1:
        return 0
    else:
        g = gcd(w, h)

        giul = h / w
        base = 0
        total = 0
        for i in range(1, w // g):
            tmp = giul * i

            total += int(tmp) + 1 - base
            base = int(tmp)
        total += (h // g) - base

        return answer - total * g


