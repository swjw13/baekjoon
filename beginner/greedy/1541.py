# 괄호를 쳐서 값을 최소로 만드는 방법

st = input()
i = 0

while st[i] == "0":
    i += 1
ans = "("
while True:
    if i == len(st):
        break
    if st[i] == "-":
        ans += ")" + st[i]
        if st[i + 1] == "0":
            while st[i + 1] == "0":
                i += 1
        ans += "("

    elif st[i] == "+":
        ans += st[i]
        while st[i+1] == "0":
            i += 1
    else:
        ans += st[i]

    i += 1
ans += ")"
print(eval(ans))
