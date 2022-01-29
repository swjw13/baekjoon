ans = set()

for i in range(10):
    a = int(input())

    ans.add(a % 42)
print(len(ans))