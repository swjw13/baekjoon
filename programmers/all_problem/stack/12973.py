# 짝지어 제거하기
# https://programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    n = len(s)
    palindrome = [False for _ in range(n)]

    stack = []
    for i in range(n - 1):
        if not palindrome[i]:
            stack.append(s[i])

            if s[i] == s[i + 1]:
                tmp = i + 1
                while stack and tmp < n:
                    if stack[-1] == s[tmp]:
                        stack.pop()
                        palindrome[tmp] = True
                        tmp += 1
                    else:
                        break
    if not palindrome[-1]:
        return 0
    elif len(stack) == 0:
        return 1
    else:
        return 0

s = "baaba"
print(solution(s))
