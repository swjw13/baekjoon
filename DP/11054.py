# 가장 긴 바이토닉 부분 수열

def lis(lst, N):
    ans_front = [1 for _ in range(N)]
    for i in range(1, N):
        for j in range(i):
            if lst[j] < lst[i]:
                ans_front[i] = max(ans_front[j] + 1, ans_front[i])
    ans_back = [1 for _ in range(N)]
    for i in range(N - 1, -1, -1):
        for j in range(i, N):
            if lst[j] < lst[i]:
                ans_back[i] = max(ans_back[j] + 1, ans_back[i])
    mx = 0
    for i in range(N):
        if ans_front[i] + ans_back[i] > mx:
            mx = ans_front[i] + ans_back[i]
    return mx


N = int(input())
lst = list(map(int, input().split()))

print(lis(lst, N)-1)
