N, X = list(map(int, input().split()))
lst = list(map(int, input().split()))

answer = [x for x in lst if x < X]
for i in answer:
    print(i, end = ' ')