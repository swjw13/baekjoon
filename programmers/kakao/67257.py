# 수식 최대화
# https://programmers.co.kr/learn/courses/30/lessons/67257
# kakao 2020

from itertools import permutations


# [-100 -200 20]
# [ * +]

def solution(expression):
    answer = 0

    numbers = []
    exps = []

    tmp = 0
    prev = 0
    while tmp < len(expression):
        if expression[tmp] in ["-", "*", "+"]:
            numbers.append(expression[prev:tmp])
            exps.append(expression[tmp])
            tmp += 1
            prev = tmp
        else:
            tmp += 1
    numbers.append(expression[prev:])
    mx = 0
    for i in permutations(["-", "*", "+"]):
        numbers_tmp = []
        exp_tmp = []

        for t in numbers:
            numbers_tmp.append(t)
        for t in exps:
            exp_tmp.append(t)

        for ex in i:
            idx = 0
            while idx < len(exp_tmp):
                print(numbers_tmp, exp_tmp)
                if exp_tmp[idx] == ex:
                    a = numbers_tmp.pop(idx)
                    b = numbers_tmp.pop(idx)
                    e = exp_tmp.pop(idx)
                    res = eval(a + e + b)
                    numbers_tmp.insert(idx, str(res))
                else:
                    idx += 1
        mx = max(mx, abs(int(numbers_tmp[0])))

    return mx


