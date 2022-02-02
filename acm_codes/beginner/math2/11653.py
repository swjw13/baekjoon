import time

N = int(input())


def is_prime(num):
    check = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            check += 1
    if num == 1:
        return False
    elif check == 1:
        return True
    else:
        return False


while N > 1:
    if is_prime(N):
        print(N)
        break
    for i in range(2, N + 1):
        if is_prime(i) and N % i == 0:
            print(i)
            N //= i
            break
