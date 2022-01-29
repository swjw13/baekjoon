N = int(input())
numbers = list(map(int, input().split()))


def is_prime(num):
    check = 0
    for i in range(1, num):
        if num % i == 0:
            check += 1
    if num == 1:
        return False
    elif check == 1:
        return True
    else:
        return False


ans = 0
for num in numbers:
    if is_prime(num):
        ans += 1
print(ans)
