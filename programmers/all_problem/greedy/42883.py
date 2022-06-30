# https://programmers.co.kr/learn/courses/30/lessons/42883
# 큰 수 만들기

def solution(number, k):
    number = list(number)
    lst = [number.pop(0)]
    for n in number:
        if lst[-1] < n:
            while len(lst) > 0 and lst[-1] < n and k > 0:
                lst.pop()
                k -= 1
            lst.append(n)

        else:
            lst.append(n)

    if k:
        lst = lst[:-k]
    return "".join(lst)

a = "1231234"
b = 3
print(solution(a, b))