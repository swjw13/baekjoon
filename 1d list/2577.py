a = int(input())
b = int(input())
c = int(input())

total = a * b * c
for i in range(10):
    num = [j for j in str(total) if j == str(i)]
    print(len(num))