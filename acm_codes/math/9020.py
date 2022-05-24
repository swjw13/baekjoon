import sys

a = [i for i in range(20001)]
a[1] = 0
for i in range(2, int(20001 ** 0.5) + 1):
    if a[i] != 0:
        tmp = 2 * i
        while tmp < 20001:
            a[tmp] = 0
            tmp += i
prime = [i for i in a if i != 0]


def find_prime(num, start, end):
    if start > end:
        return False
    mid = (start + end) // 2
    if prime[mid] == num:
        return True
    elif prime[mid] > num:
        return find_prime(num, start, mid - 1)
    else:
        return find_prime(num, mid + 1, end)


t = int(input())
prime_length = len(prime)
for _ in range(t):
    n = int(sys.stdin.readline())
    for i in range(n // 2, 0, -1):
        if find_prime(i, 0, prime_length) and find_prime(n - i, 0, prime_length):
            print(i, n - i)
            break
