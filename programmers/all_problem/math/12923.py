# https://programmers.co.kr/learn/courses/30/lessons/12923
# 숫자 블록

def get_prime(n):
    tmp = [i for i in range(n + 1)]
    for i in range(2, int(n ** 0.5) + 1):
        a = 2 * i
        while a < n + 1:
            tmp[a] = 0
            a += i
    ans = []
    for i in tmp:
        if i != 0:
            ans.append(i)
    return ans[1:]


lst = get_prime(int(1000000000 ** 0.5) + 1)


def solution(begin, end):
    answer = []

    for i in range(begin, end + 1):
        a = 1
        tmp = [j for j in lst if j < i]
        cur_num = i
        for t in tmp:
            check = False
            while cur_num % t == 0:
                cur_num //= t
                if cur_num < 10000000:
                    check = True
                    a = cur_num
                    break
            if check:
                break


        answer.append(a)

    if begin == 1:
        answer[0] = 0

    return answer


print(solution(1, 10))
