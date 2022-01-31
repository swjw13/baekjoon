# 균형 잡힌 문자열

while True:
    string = input()
    if string == ".":
        break
    stack = []
    tmp = 0

    for i in string:
        if i == '[':
            stack.append('[')
        elif i == '(':
            stack.append('(')
        elif i == ']':
            if len(stack) == 0:
                tmp = 1
                break
            elif stack[-1] == "(":
                tmp = 1
                break
            else:
                stack.pop()
        elif i == ')':
            if len(stack) == 0:
                tmp = 1
                break
            elif stack[-1] == "[":
                tmp = 1
                break
            else:
                stack.pop()

    if tmp == 1:
        print("no")
    else:
        if len(stack) != 0:
            print("no")
        else:
            print("yes")
