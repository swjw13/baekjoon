# https://www.acmicpc.net/problem/20047
# 동전 옮기기

N = int(input())
S = list(input())
T = list(input())

p1, p2 = list(map(int, input().split()))

if S == T:
    print("YES")
else:
    buffer = [S[p1], S[p2]]
    S.pop(p2)
    S.pop(p1)

    S_idx = N - 3
    T_idx = N - 1
    buffer_idx = 1

    answer = True

    while T_idx >= 0:
        if S_idx < 0 or S[S_idx] != T[T_idx]:
            if buffer_idx < 0 or T[T_idx] != buffer[buffer_idx]:
                answer = False
                break
            else:
                buffer_idx -= 1
                T_idx -= 1
        else:
            S_idx -= 1
            T_idx -= 1

    if answer:
        print("YES")
    else:
        print("NO")
