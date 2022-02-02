# 괄호 문자열

N = int(input())

for _ in range(N):
    ans = 0
    stack = []
    string = input()
    for i in string:
        if i == "(":
            stack.append(1)
        else:
            if len(stack) == 0:
                ans = 1
                break
            else:
                stack.pop()
    if len(stack) != 0:
        ans = 1
    if ans == 1:
        print("NO")
    else:
        print("YES")