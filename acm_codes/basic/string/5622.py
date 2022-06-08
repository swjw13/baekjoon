nums = dict()
alphas = ['ABC', "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

for i in range(len(alphas)):
    for j in alphas[i]:
        nums[j] = i + 3

S = input()
total = 0
for i in S:
    total += nums[i]
print(total)
