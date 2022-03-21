# 후보키
# https://programmers.co.kr/learn/courses/30/lessons/42890
# kakao 2019

from itertools import combinations


def solution(relation):
    answer = []

    total_student = len(relation)
    col_number = len(relation[0])
    col_tmp = [i for i in range(col_number)]

    for i in range(1, col_number + 1):
        for iters in combinations(col_tmp, i):
            tmp = set()

            for each_student in relation:
                key = ""
                for cols in iters:
                    key += str(each_student[cols])
                tmp.add(key)

            if len(tmp) == total_student:
                ans = True
                to_check = set(iters)
                for prevs in answer:
                    if len(prevs - to_check) == 0:
                        ans = False
                        break
                if ans:
                    answer.append(to_check)

    return len(answer)


a = [['a', 1, 'aaa', 'c', 'ng'], ['b', 1, 'bbb', 'c', 'g'], ['c', 1, 'aaa', 'd', 'ng'], ['d', 2, 'bbb', 'd', 'ng']]
print(solution(a))
