def fractal(n, k):
    if n == 1:
        print("*", end="")
    else:
        if k <= n // 3:
            fractal(n // 3, k)
            fractal(n // 3, k)
            fractal(n // 3, k)
        elif k <= (2 * n) // 3:
            fractal(n // 3, k - (n // 3))
            for _ in range(1, n // 3 + 1):
                print(" ", end="")
            fractal(n // 3, k - (n // 3))
        else:
            fractal(n // 3, k - ((2 * n) // 3))
            fractal(n // 3, k - ((2 * n) // 3))
            fractal(n // 3, k - ((2 * n) // 3))


n = int(input())
for i in range(1, n + 1):
    fractal(n, i)
    print()
