T = int(input())

for i in range(T):
    H, W, N = list(map(int, input().split()))
    width = (N-1) // H + 1
    height = (N-1) % H + 1

    print(height * 100 + width)