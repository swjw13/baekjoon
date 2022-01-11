def fact(num):
    total = 1
    for i in range(1, num + 1):
        total *= i
        # total %= 10007
    return total


N, K = list(map(int, input().split()))

print((fact(N) // (fact(K) * fact(N - K))) % 10007)
