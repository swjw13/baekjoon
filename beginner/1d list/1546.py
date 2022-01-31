N = int(input())
scores = list(map(int, input().split()))

max = max(scores)

new_total = 0
for i in range(N):
    new_total += scores[i] / max * 100

print("%.6f"%(new_total/N))