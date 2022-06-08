N = int(input())

for _ in range(N):
    R, S = input().split()

    ans = ""
    for i in S:
        ans += i * int(R)
    print(ans)