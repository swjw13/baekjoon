max_value = 0
answer = [-1]


def solution(n, info):
    def get_list(remain_num, lst):
        global max_value, answer
        if len(lst) == 10:
            lst.append(remain_num)

            apeach = 0
            ryan = 0
            for i in range(11):
                if info[i] > lst[i]:
                    apeach += (10 - i)
                elif info[i] == lst[i]:
                    if info[i] != 0:
                        apeach += (10 - i)
                else:
                    ryan += (10 - i)

            if ryan - apeach > max_value:
                max_value = ryan - apeach
                answer = lst
            elif ryan - apeach == max_value:
                if max_value != 0:
                    for i in range(10, -1, -1):
                        if answer[i] < lst[i]:
                            answer = lst
                            break
                        elif answer[i] > lst[i]:
                            break
        else:
            for i in range(remain_num, -1, -1):
                get_list(remain_num - i, lst + [i])

    get_list(n, [])

    return answer


n = 10
a = [0,0,0,0,0,0,0,0,3,4,3]
print(solution(n, a))
