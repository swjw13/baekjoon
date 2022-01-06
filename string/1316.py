def check(st):
    check = [0 for _ in range(26)]
    check[ord(st[0]) - ord('a')] += 1
    for i in range(1, len(st)):
        if st[i] is not st[i - 1]:
            if check[ord(st[i]) - ord('a')] == 0:
                check[ord(st[i]) - ord('a')] += 1
            else:
                return False

    return True

total = 0
N = int(input())
for _ in range(N):
    s = input()
    if check(s):
        total += 1

print(total)
