N = int(input())

total = 0
start = 665
while True:
    if '666' in str(start):
        total += 1
        if total == N:
            print(start)
            break
    start += 1
