# 괄호 변환
# https://programmers.co.kr/learn/courses/30/lessons/60058
# kakao 2020

def solution(p):

    def right_shape(st):
        ans = 0
        for i in range(len(st)):
            if st[i] == "(":
                ans += 1
            else:
                ans -= 1
            if ans < 0:
                return False
        return True

    if len(p) == 0:
        return ""

    tmp = 1
    while tmp < len(p):
        if p[:tmp].count(")") == p[:tmp].count("("):
            break
        else:
            tmp += 1

    u = p[:tmp]
    v = p[tmp:]

    if right_shape(u):
        v_prime = solution(v)
        return u + v_prime
    else:
        tmp = "("
        tmp += solution(v)
        tmp += ")"

        u = u[1:-1]
        u_prime = ""
        for i in range(len(u)):
            if u[i] == "(":
                u_prime += ")"
            else:
                u_prime += "("
        tmp += u_prime

        return tmp

