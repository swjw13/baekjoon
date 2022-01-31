import sys

input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
T = int(input())

mapping = [[0 for _ in range(N)] for _ in range(N)]

i = 0
while i < N:
    start = int(i)
    end = int(i + 0.5)
    tmp = 0
    while start >= 0 and end < N:
        if tmp == 0:
            if lst[start] == lst[end]:
                mapping[start][end] = 1
            else:
                tmp = 1
                mapping[start][end] = 0
        else:
            mapping[start][end] = 0
        start -= 1
        end += 1
    i += 0.5


for _ in range(T):
    num1, num2 = list(map(int, input().split()))
    print(mapping[num1-1][num2-1])
