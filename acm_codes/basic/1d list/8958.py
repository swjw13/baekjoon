N = int(input())

for i in range(N):
    score = 0
    ans = input()
    for i in ans.split("X"):
        for j in range(len(i)):
            score += j + 1
    print(score)
