N = int(input())
cycle = 0
new_number = N

while True:
    new_number = (new_number % 10) * 10 + (new_number // 10 + new_number % 10) % 10
    cycle += 1
    if new_number == N:
        break

print(cycle)
